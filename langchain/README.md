# langchain

LangChain v1 案例：用 `create_agent` 构建 Agent，并演示**流式输出显示**。

## 项目结构

| 路径 | 作用 |
| --- | --- |
| `src/HelloLangchainAgent.py` | **案例一（入门）**：带 `get_weather` 工具的最小 Agent，演示调用与流式输出 |
| `src/RealWorldAgent.py` | **案例二（实战）**：抓取 URL 文档 + `InMemorySaver` 多轮记忆的文学数据助手 |
| `.env.example` | 环境变量参考模板（占位符，随项目提交） |
| `.env` | 真实环境变量配置（含密钥，被 `.gitignore` 忽略，**不提交**；由 `.env.example` 复制生成） |
| `main.py` | `uv init` 生成的默认入口（打印 Hello from langchain!），无实际用途 |
| `pyproject.toml` | 项目元数据与依赖声明 |
| `uv.lock` | uv 依赖锁文件（锁定精确版本，保证可复现） |
| `.python-version` | 项目 Python 版本约束（3.12） |
| `.venv/` | 项目虚拟环境（`uv sync` 自动生成，无需手动管理） |

## 环境准备

### 1. 安装依赖

```shell
uv init
uv add langchain langchain-openai langgraph
uv sync
```

> ⚠️ **注意**：两个案例都用 `langchain.agents.create_agent`，案例二还用
> `langgraph.checkpoint.memory.InMemorySaver`，因此必须**同时安装 `langchain` 与 `langgraph`**，
> 仅声明 `langchain-openai` 会因缺包而运行失败。

### 2. 配置环境变量（推荐：.env 文件）

两个案例统一从环境变量读取配置（`OPENAI_API_KEY` / `OPENAI_API_BASE` 缺失时启动即报错）。

**第一步：复制参考模板并填入真实值**

```shell
# 在 langchain/ 目录下执行
copy .env.example .env      # Windows
# cp .env.example .env      # macOS / Linux
```

```dotenv
# 编辑 .env，把占位符替换为真实值
OPENAI_API_KEY=your-api-key
OPENAI_API_BASE=your-api-url
OPENAI_MODEL=deepseek-v4-flash
```

> 🔒 **提交约定**：`.env` 含真实密钥，已由根目录 `.gitignore` 忽略、**绝不提交**；
> `.env.example` 是占位符模板，随项目提交供参考。改动模板请改 `.env.example`，不要提交 `.env`。

**环境变量一览**

| 环境变量 | 必填 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `OPENAI_API_KEY` | ✅ | API 密钥 | — |
| `OPENAI_API_BASE` | ✅ | API 地址（OpenAI 兼容接口） | — |
| `OPENAI_MODEL` | ❌ | 模型名 | `deepseek-v4-flash` |
| `LANGSMITH_TRACING` | ❌ | 是否开启 LangSmith 追踪（`true`/`false`） | 关闭 |
| `LANGSMITH_API_KEY` | 追踪时 ✅ | LangSmith API Key | — |
| `LANGSMITH_PROJECT` | ❌ | LangSmith 项目名（按项目分组） | 默认项目 |

> 不想用文件时，也可以临时在终端设置：
>
> ```shell
> # Windows (cmd)
> set OPENAI_API_KEY=your-api-key
> set OPENAI_API_BASE=your-api-url
> set OPENAI_MODEL=deepseek-v4-flash
>
> # macOS / Linux
> export OPENAI_API_KEY="your-api-key"
> export OPENAI_API_BASE="your-api-url"
> export OPENAI_MODEL="deepseek-v4-flash"
> ```

### 3. IDEA / PyCharm 加载 .env（快捷方式）

1. 打开要运行的案例文件（如 `src/HelloLangchainAgent.py`）
2. 点击右上角运行配置下拉框 → **Edit Configurations...**
3. **新版 IDEA / PyCharm（2023.1+）**：**Modify options** → 勾选 **Environment file** →
   选择 `langchain/.env`（原生支持，无需插件）
4. **旧版**：Settings → Plugins 安装 **EnvFile** 插件 → Edit Configurations → 勾选 **EnvFile** → 添加 `.env`
5. Apply / OK 后直接运行，无需终端 export

> 也可以直接在运行配置的 **Environment variables** 一栏手填（多条用分号 `;` 分隔）：
> `OPENAI_API_KEY=xxx;OPENAI_API_BASE=xxx;OPENAI_MODEL=deepseek-v4-flash`

## 案例一：HelloLangchainAgent.py（入门）

位置：`src/HelloLangchainAgent.py`

创建一个带 `get_weather` 工具的最小 Agent，调用一次并输出结果。

### 普通调用（invoke）

```python
from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model=f"openai:{model}",               # 模型名从环境变量 OPENAI_MODEL 读取
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
    debug=True,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```

### 流式输出（stream）

把 `invoke` 换成 `stream`，用 `stream_mode="messages"` 逐 token 打印（打字机效果）：

```python
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    stream_mode="messages",
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]   # token 是 AIMessageChunk
        if token.text:
            print(token.text, end="", flush=True)
```

## 案例二：RealWorldAgent.py（实战）

位置：`src/RealWorldAgent.py`

一个「文学数据助手」：通过 `fetch_text_from_url` 工具抓取 Project Gutenberg 上的
《了不起的盖茨比》全文，回答「包含 Gatsby 的行数 / Daisy 首次出现的行号」等问题；
用 `InMemorySaver` 作为 checkpointer，按 `thread_id` 保存多轮会话。

### 普通调用（invoke）

```python
# ...（agent 构建部分见源文件：init_chat_model + @tool + InMemorySaver）

agent_result = agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-lc"}},
)
print(agent_result["messages"][-1].content_blocks)
```

### 流式输出（stream）

同时监听 token 流与 Agent 每步状态（工具调用、节点执行进度）：

```python
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-lc"}},
    stream_mode=["messages", "updates"],
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]
        if token.text:
            print(token.text, end="", flush=True)
    elif chunk["type"] == "updates":
        for node, update in chunk["data"].items():
            if node in ("model", "tools"):
                msg = update["messages"][-1]
                print(f"\n—— [{node}] 完成: {msg.__class__.__name__}", flush=True)
```

## 流式输出（Streaming）说明

`create_agent` 返回的是一个 LangGraph 编译图，天然支持 `stream()` / `astream()`，
配合 `stream_mode` 控制输出内容：

| stream_mode | 作用 |
| --- | --- |
| `messages` | 流式输出 LLM 生成的 token（`AIMessageChunk`），`chunk["data"]` 为 `(token, metadata)` 元组 |
| `updates` | 每个 Agent 步骤完成后的状态更新（`model` 节点 / `tools` 节点） |
| `custom` | 工具内部通过 `get_stream_writer()` 主动推送的进度信息 |
| `debug` | 每次运行完整状态流的调试输出（见下节） |

推荐加 `version="v2"`：输出统一为 `{"type", "ns", "data"}` 的 StreamPart 结构，
方便按 `chunk["type"]` 分支处理，也可以同时传多个模式（如 `["messages", "updates"]`）。

- 只想要「打字机」效果 → `stream_mode="messages"`，打印 `token.text`
- 还想显示工具调用/执行进度 → `stream_mode=["messages", "updates"]`
- 想在工具执行中推送「正在抓取第 N 行…」这类进度 → `stream_mode="custom"` + 工具内 `get_stream_writer()`

## 调试与追踪（Debug & Trace）

### 1. `debug=True`：终端日志

`create_agent(..., debug=True)` 会在**终端打印每一步执行日志**——模型调用、工具调用、
消息如何在 Agent 各节点间流转，适合本地快速排查。

- 案例一：已开启
- 案例二：默认关闭（源码中 `debug=True` 已注释），按需打开即可

### 2. LangSmith：全链路可视化追踪

LangSmith 会把**所有环节**（LLM 调用、工具执行、Agent 步骤、token 用量、耗时）自动上报到
云端控制台，可按时间线查看每一步的输入/输出，定位问题最高效。

只需在 `.env` 中打开（**无需改代码**，venv 已随 `langchain-openai` 装上 `langsmith`）：

```dotenv
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=langchain-examples   # 可选，按项目分组
```

运行案例后，到 LangSmith 控制台按 project 查看每次运行的完整链路。
对应关系：`.env` 中 `LANGSMITH_*` 触发 tracing → langchain/langgraph 自动打点 →
控制台可视化展示每个环节。

### 3. 终端兜底：`stream_mode="debug"`

不开 LangSmith 时，可用 `stream_mode="debug"` 在终端打印每次运行的完整状态流：

```python
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    stream_mode="debug",
    version="v2",
):
    print(chunk["type"], chunk["data"])
```

## 官方文档

- Streaming：<https://docs.langchain.com/oss/python/langchain/streaming>
- Agent：<https://docs.langchain.com/oss/python/langchain/agents>
