# from dotenv import load_dotenv
# import os

# load_dotenv("../.env")

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# MODEL_NAME = os.getenv(
#     "MODEL_NAME",
#     "gpt-4o-mini"
# )

# print("KEY LOADED:", OPENAI_API_KEY[:15] if OPENAI_API_KEY else None)

 

from dotenv import load_dotenv
import os

load_dotenv("../.env")

LM_STUDIO_URL = os.getenv(
    "LM_STUDIO_URL",
    "http://127.0.0.1:1234/v1"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "local-model"
)