from pathlib import Path
import traceback

from fastapi import APIRouter

from models.quiz_models import (
    QuizRequest,
    QuizResponse
)

from services.quiz_service import (
    QuizService
)

router = APIRouter()

quiz_service = QuizService()


@router.post(
    "/generate-quiz",
    response_model=QuizResponse
)
def generate_quiz(
    request: QuizRequest
):

    try:

        file_path = Path(
            f"data/extracted/{request.document_name}.txt"
        )

        print("QUIZ FILE:", file_path)

        text = file_path.read_text(
            encoding="utf-8"
        )

        quiz = quiz_service.generate_quiz(
            text=text,
            questions_count=request.questions_count
        )

        return QuizResponse(
            quiz=quiz
        )

    except Exception as e:

        print("\n===== QUIZ ERROR =====")
        print(type(e))
        print(str(e))
        traceback.print_exc()
        print("======================\n")

        raise