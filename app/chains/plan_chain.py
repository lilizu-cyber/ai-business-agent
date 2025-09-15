from langchain.llms import OpenAI
from app.utils.prompts import PLAN_PROMPT
from app.config import OPENAI_API_KEY


def generate_plan(idea: str):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY,
                 temperature=0.3, max_tokens=600)
    prompt = PLAN_PROMPT.format(idea=idea)
    response = llm(prompt)
    return response.strip()
