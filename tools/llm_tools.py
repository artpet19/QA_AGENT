
from agent import QuestionAnsweringAgent
from tools.web_search import web_search

class LLMTool:
    def __init__(self):
        self.agent = QuestionAnsweringAgent()

    def handle_query(self, query):
        """Returns AI-generated answers + web search results"""
        ai_response = self.agent.ask(query)
        web_results = web_search(query)

        response = {
            "AI Answer": ai_response,
            "Web Sources": web_results
        }
        return response