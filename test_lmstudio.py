from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {
            "role": "user",
            "content": "ETF چیست؟"
        }
    ]
)

print(response.choices[0].message.content)

from services.llm_service import LLMService

llm = LLMService()

answer = llm.ask(
    "ETF چیست؟"
)

print(answer)