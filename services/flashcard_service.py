from services.llm_service import LLMService


class FlashcardService:

    def __init__(self):

        self.llm = LLMService()

    def generate_flashcards(
        self,
        text: str,
        count: int = 10
    ):

        prompt = f"""
از متن زیر {count} فلش کارت آموزشی بساز.

فرمت:

کارت 1

سوال:
...

پاسخ:
...

کارت 2

سوال:
...

پاسخ:
...

متن:

{text[:12000]}
"""

        return self.llm.ask(prompt)