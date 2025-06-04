import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize the model
model = HfApiModel()

# Define tools (DuckDuckGo for web search)
tools = [DuckDuckGoSearchTool()]

# Create the agent
agent = CodeAgent(tools=tools, model=model, additional_authorized_imports=["requests", "bs4"])

def web_search(query):
    """Perform a web search using SmolAgents."""
    result = agent.run(query)
    return result