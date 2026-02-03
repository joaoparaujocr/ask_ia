from langchain_openai import ChatOpenAI
from core.settings import settings
from core.llm.base import LLMProvider

class OpenAILLMProvider(LLMProvider):
    def get_llm(self):
        return ChatOpenAI(
            api_key=settings.openai_api_key,
            model=settings.openai_model,
            temperature=0.4,
        )

def get_llm():
    return OpenAILLMProvider().get_llm()
