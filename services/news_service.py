from services.llm_service import LLMService


class NewsService:

    def __init__(self):

        self.llm = LLMService()

    def analyze(
        self,
        news_text: str
    ):

        prompt = f"""
شما یک تحلیلگر بازار سرمایه هستید.

خبر زیر را تحلیل کن.

خروجی شامل:

1- خلاصه خبر

2- نکات مهم

3- ریسک های احتمالی

4- فرصت های احتمالی

5- جمع بندی

خبر:

{news_text}
"""

        return self.llm.ask(
            prompt
        )