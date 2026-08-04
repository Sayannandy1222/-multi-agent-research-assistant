import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://redis:6379",
)