from fastapi import FastAPI
from app.chains.idea_chain import generate_ideas
from app.chains.market_chain import market_research
from app.chains.plan_chain import generate_plan
from app.chains.landing_chain import generate_landing_copy

app = FastAPI(title="AI Business Agent")


@app.get("/")
def root():
    return {"message": "🚀 AI Business Agent is running"}


@app.get("/ideas")
def ideas(industry: str = "SaaS"):
    return {"industry": industry, "ideas": generate_ideas(industry)}


@app.get("/market")
def market(industry: str = "SaaS"):
    return {"industry": industry, "research": market_research(industry)}


@app.get("/plan")
def plan(idea: str = "HR SaaS for mid-sized companies"):
    return {"idea": idea, "plan": generate_plan(idea)}


@app.get("/landing")
def landing(idea: str = "HR SaaS for mid-sized companies"):
    return {"idea": idea, "landing_copy": generate_landing_copy(idea)}
