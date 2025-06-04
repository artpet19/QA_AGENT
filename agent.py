import os
from dotenv import load_dotenv

from transformers import pipeline
#from transformers import AutoModelForCausalLM
from huggingface_hub import login

login(token = os.getenv("HUGGINGFACEHUB_API_TOKEN"))



load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")

#model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
#model.to("cuda")

class QuestionAnsweringAgent:
    def __init__(self):
        self.qa_pipeline = pipeline("text-generation", model=MODEL_NAME)
        self.memory = []  # Track conversation history

    def format_prompt(self, query):
        """Enhance prompt clarity for better response accuracy"""
        prompt = f"You are a helpful AI assistant. Answer the following question concisely:\n\nQuestion: {query}\nAnswer:"
        return prompt

    def ask(self, query):
        formatted_query = self.format_prompt(query)
        response = self.qa_pipeline(formatted_query, max_length=100, temperature=0.7)
        
        # Store conversation history
        self.memory.append({"query": query, "response": response[0]['generated_text'].strip()})
        
        return response[0]['generated_text'].strip()

    def get_history(self):
        """Retrieve recent conversation history"""
        return self.memory[-5:]  # Show last five exchanges