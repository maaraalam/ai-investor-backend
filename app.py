from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router
from routes.pdf import router as pdf_router
from routes.rag import router as rag_router
from routes.quiz import router as quiz_router
from routes.summary import router as summary_router
from routes.flashcard import router as flashcard_router
from routes.news import router as news_router
from routes.history import router as history_router
from routes.auth import router as auth_router


app = FastAPI(title="AI Investor Assistant")





# 🔥 MUST BE FIRST middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 👈 تستی (برای اینکه 100% کار کند)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)
app.include_router(pdf_router)
app.include_router(rag_router)
app.include_router(quiz_router)
app.include_router(summary_router)
app.include_router(flashcard_router)
app.include_router(news_router)
app.include_router(history_router)
app.include_router(auth_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "ok"}