import os

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
    # 返回固定格式的天气信息（示例中始终返回晴天）
    return f"It's always sunny in {city}!"


# 创建一个智能体实例
agent = create_agent(
    model=f"openai:{model}",           # 指定使用的模型（OpenAI 兼容接口，模型名从环境变量读取）
    tools=[get_weather],               # 注册工具列表，这里只注册了天气查询工具
    system_prompt="You are a helpful assistant",  # 系统提示词，定义智能体的角色和行为
    debug=True,                        # 开启调试模式，会输出详细的执行日志
)

# 调用智能体，传入用户消息（询问旧金山的天气）
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

# 打印智能体回复的最后一条消息的内容块（即最终生成的回答）
print(result["messages"][-1].content_blocks)
