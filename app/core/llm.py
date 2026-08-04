from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY


def get_llm(
    temperature: float = 0,
):
    """
    Returns a configured Groq LLM instance.
    """

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY,
        temperature=temperature,
    )