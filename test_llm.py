from services.llm_service import LLMService

llm = LLMService()

prompt = """
از متن زیر 2 سوال چهارگزینه‌ای بساز.

ETF صندوق قابل معامله در بورس است.
سرمایه‌گذاران می‌توانند واحدهای آن را خرید و فروش کنند.
"""

print(
    llm.ask(prompt)
)