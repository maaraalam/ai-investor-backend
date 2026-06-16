from services.llm_service import LLMService


class SummaryService:

    def __init__(self):

        self.llm = LLMService()

    def summarize(
        self,
        text: str
    ):

        prompt = f"""
متن زیر را خلاصه کن.

خروجی شامل:

1- خلاصه اجرایی

2- مهمترین نکات

3- مفاهیم کلیدی

متن:

{text[:12000]}
"""

        return self.llm.ask(
            prompt
        )