
# app.py
# This script sets up a Gradio interface for handling user queries using an LLM tool.

import gradio as gr
from tools.llm_tools import LLMTool

def handle_query(query):
    if query.lower() == "exit":
        return "Goodbye!"
    
    llm_tool = LLMTool()
    response = llm_tool.handle_query(query)
    
    ai_answer = response.get("AI Answer", "No response available.")
    web_sources = response.get("Web Sources", "No sources found.")
    
    return f"**AI Answer:** {ai_answer}\n\n🔎 **Web Search Results:**\n{web_sources}"

demo = gr.Interface(fn=handle_query, inputs="text", outputs="text")
demo.launch()