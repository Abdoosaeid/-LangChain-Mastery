import os
from typing import Dict, Any
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
# Note: Ensure you are using the correct agent creator for your LangGraph version
from langgraph.prebuilt import create_react_agent 

load_dotenv()

# 1. Setup the LLM
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# 2. Setup the Tools
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for recipe information."""
    return tavily.search(query)

# 3. Define the System Prompt
system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""
# 4. Create the Agent
# In modern LangGraph, we use create_react_agent
agent = create_react_agent(
    model=model,
    tools=[web_search],
    state_modifier=system_prompt
)