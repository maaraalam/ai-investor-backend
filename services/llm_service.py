from openai import OpenAI

from services.chat_memory_service import (
    ChatMemoryService
)


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            base_url="http://127.0.0.1:1234/v1",
            api_key="lm-studio"
        )

        self.memory = ChatMemoryService()

    def ask(
        self,
        question: str
    ):

        self.memory.add_user_message(
            question
        )

        messages = [
            {
                "role": "system",
                "content": """
شما مدرس حرفه‌ای بازار سرمایه هستید.
به فارسی پاسخ بده.
کوتاه و دقیق پاسخ بده.
"""
            }
        ]

        messages.extend(
            self.memory.get_messages()
        )

        response = (
            self.client.chat.completions.create(
                model="qwen2.5-3b-instruct",
                messages=messages,
                temperature=0.2,
                max_tokens=120
            )
        )

        answer = (
            response
            .choices[0]
            .message.content
        )

        self.memory.add_assistant_message(
            answer
        )

        return answer

    def clear_memory(
        self
    ):

        self.memory.clear()