from langchain.llms import OpenAI
from app.utils.prompts import MARKET_PROMPT
from app.config import OPENAI_API_KEY


def market_research(industry: str):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY,
                 temperature=0.4, max_tokens=400)
    prompt = MARKET_PROMPT.format(industry=industry)
    response = llm(prompt)
    return response.strip()
