from services.llm_service import (
    LLMService
)


class QuizService:

    def __init__(self):

        self.llm = LLMService()

    def generate_quiz(
        self,
        text: str,
        questions_count: int = 2
    ):

        text = text[:1000]

        prompt = f"""
از متن زیر فقط {questions_count} سوال چهار گزینه‌ای بساز.

متن:

{text}
"""

        print("Sending to LLM...")

        result = self.llm.ask(
            prompt
        )

        print("LLM Response Received")

        return result