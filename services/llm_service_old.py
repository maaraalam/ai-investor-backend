from openai import OpenAI


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            base_url="http://127.0.0.1:1234/v1",
            api_key="lm-studio"
        )

    def ask(self, question: str):

        response = self.client.chat.completions.create(
            model="qwen2.5-3b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "شما مدرس بازار سرمایه هستید. کوتاه و فارسی جواب بده."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.2,
            max_tokens=120
        )

        return response.choices[0].message.content