import os
import urllib.error
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

# 加载项目根目录的 .env（真实密钥不提交，参考 .env.example）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
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

SYSTEM_PROMPT = """You are a literary data assistant.

## Capabilities

- `fetch_text_from_url`: loads document text from a URL into the conversation.
Do not guess line counts or positions—ground them in tool results from the saved file."""


@tool
def fetch_text_from_url(url: str) -> str:
    """Fetch the document from a URL and compute exact line statistics for the requested counts."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    text = raw.decode("utf-8", errors="replace")

    # 在工具内部用 Python 精确统计，避免把整本书塞进上下文让模型硬数
    lines = text.splitlines()
    gatsby_line_count = sum(1 for line in lines if "Gatsby" in line)
    daisy_first_line = next(
        (i + 1 for i, line in enumerate(lines) if "Daisy" in line),
        None,
    )

    # 定位正文起点（跳过 Gutenberg 文件头），供写 synopsis 参考
    start_idx = 0
    for i, line in enumerate(lines):
        if "START OF THE PROJECT GUTENBERG EBOOK" in line:
            start_idx = i + 1
            break
    preview = "\n".join(lines[start_idx : start_idx + 60])

    return (
        f"Fetched {len(raw)} bytes, {len(lines)} lines total.\n"
        f"gatsby_line_count = {gatsby_line_count}\n"
        f"daisy_first_line (1-based) = {daisy_first_line}\n"
        f"--- text preview (first 60 lines of the book body, for the synopsis) ---\n{preview}"
    )


chat_model = init_chat_model(
    f"openai:{model}",  # 指定使用的模型（OpenAI 兼容接口，模型名从环境变量读取）
    temperature=0.5,
    timeout=300,
    max_tokens=2048,
)

checkpointer = InMemorySaver()


agent = create_agent(
    model=chat_model,
    tools=[fetch_text_from_url],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
    # debug=True,   # 需要本地调试时打开：会在终端打印每一步执行日志
)

content = f"""Project Gutenberg hosts a full plain-text copy of F. Scott Fitzgerald's The Great Gatsby.
URL: https://www.gutenberg.org/files/64317/64317-0.txt

Answer as much as you can:

1) How many lines in the complete Gutenberg file contain the substring `Gatsby` (count lines, not occurrences within a line, each line ends with a line break).
2) The 1-based line number of the first line in the file that contains `Daisy`.
3) A two-sentence neutral synopsis.

Do your best on (1) and (2). If at any point you realize you cannot **verify** an exact answer with
your available tools and reasoning, do not fabricate numbers: use `null` for that field and spell out
the limitation in `how_you_computed_counts`. If you encounter any errors please report what the error was and what the error message was."""

# ===== 流式调用（stream）：逐 token 打印 + 显示工具/节点执行进度 =====
# 对应非流式版本见 src/RealWorldAgent.py（agent.invoke）
print("=== Agent 流式输出开始（messages + updates） ===")
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-lc"}},
    stream_mode=["messages", "updates"],
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]  # token 是 AIMessageChunk
        if token.text:
            print(token.text, end="", flush=True)
    elif chunk["type"] == "updates":
        # 打印每个 Agent 步骤完成后的节点状态（model 推理 / tools 工具执行）
        for node, update in chunk["data"].items():
            if node in ("model", "tools"):
                msg = update["messages"][-1]
                print(f"\n—— [{node}] 完成: {msg.__class__.__name__}", flush=True)
print("\n=== Agent 流式输出结束 ===")
