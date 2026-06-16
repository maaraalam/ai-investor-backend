from services.llm_service import LLMService

llm = LLMService()

answer = llm.ask(
    "صندوق ETF چیست؟"
)

print(answer)