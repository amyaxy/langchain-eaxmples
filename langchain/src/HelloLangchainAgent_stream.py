import os
from pathlib import Path

from dotenv import load_dotenv

# 加载项目根目录的 .env（真实密钥不提交，参考 .env.example）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from langchain.agents import create_agent

# ===== 环境变量配置（见 README「环境准备」） =====
#   OPENAI_API_KEY  : API 密钥（必填，缺失则报错）
#   OPENAI_API_BASE : API 地址，OpenAI 兼容接口（必填，缺失则报错）
#   OPENAI_MODEL    : 模型名（可选，默认 deepseek-v4-flash）
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")
model = os.getenv("OPENAI_MODEL", "deepseek-v4-flash")

if not api_key or not api_base:
    raise RuntimeError("请先设置环境变量 OPENAI_API_KEY 和 OPENAI_API_BASE")


# 定义一个天气查询工具函数，智能体可以调用它来获取城市天气
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


# 创建一个智能体实例
agent = create_agent(
    model=f"openai:{model}",           # 指定使用的模型（OpenAI 兼容接口，模型名从环境变量读取）
    tools=[get_weather],               # 注册工具列表，这里只注册了天气查询工具
    system_prompt="You are a helpful assistant",  # 系统提示词，定义智能体的角色和行为
    debug=True,                        # 开启调试模式，会输出详细的执行日志
)

# ===== 流式调用（stream）：逐 token 打印，打字机效果 =====
# 对应非流式版本见 src/HelloLangchainAgent.py（agent.invoke）
print("=== Agent 流式输出开始 ===")
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    stream_mode="messages",
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]  # token 是 AIMessageChunk
        if token.text:
            print(token.text, end="", flush=True)
print("\n=== Agent 流式输出结束 ===")
