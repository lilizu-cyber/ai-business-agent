from langchain.llms import OpenAI
from app.utils.prompts import LANDING_PROMPT
from app.config import OPENAI_API_KEY


def generate_landing_copy(idea: str):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY,
                 temperature=0.7, max_tokens=300)
    prompt = LANDING_PROMPT.format(idea=idea)
    response = llm(prompt)
    return response.strip()
