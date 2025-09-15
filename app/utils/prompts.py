IDEA_PROMPT = """
You are a startup mentor. Generate 3 business ideas in the {industry} space.
For each idea, provide:
- Problem statement
- Customer segment
- Value proposition
- Competitor benchmark
- Monetization strategy
Rank them by feasibility and impact.
"""

MARKET_PROMPT = """
You are a market analyst. Provide a short market research summary for {industry}:
- TAM/SAM/SOM estimates
- Top 3 competitors
- Key customer needs
- Suggested 2 validation experiments
"""

PLAN_PROMPT = """
Draft a Lean Business Plan for {idea}.
Sections:
- Problem
- Solution
- Unique Value Proposition
- Revenue Streams
- Cost Structure
- Key Metrics
- Risks
Output in bullet points.
"""

LANDING_PROMPT = """
Write landing page copy for {idea}.
Include:
- Headline
- Subheadline
- 3 bullet benefits
- Call to Action
Tone: clear and inspiring.
"""
