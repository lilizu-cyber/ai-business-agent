from langchain.llms import OpenAI
from app.utils.prompts import IDEA_PROMPT
from app.config import OPENAI_API_KEY


def generate_ideas(industry: str):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY,
                 temperature=0.6, max_tokens=500)
    prompt = IDEA_PROMPT.format(industry=industry)
    response = llm(prompt)
    return response.strip()
