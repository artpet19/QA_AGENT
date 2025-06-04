# Hugging Face AI Agent 🧠🚀

## 📌 Project Overview
This project is an **LLM-powered Question-Answering Agent** designed to:
- Answer user queries using a Hugging Face model.
- Perform **live web searches** for real-time information.
- Maintain conversation memory for **context-aware responses**.

## 🚀 Features
✅ AI-powered question answering using Hugging Face models  
✅ Integrated **web search** for real-time results  
✅ Memory tracking for improved responses  
✅ Configurable response length & temperature  
✅ Optimized for **GAIA Benchmark** scoring  

## 🛠️ Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/QA_AGENT.git
cd QA_AGENT

## Install Dependencies 
pip install -r requirements.txt

## Set-up Environment variables
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_key_here
MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.1

## Usage
python app.py

## Example Interaction
User: "What is quantum computing?"
AI Agent: "Quantum computing is a computational approach using qubits to process complex algorithms."
🔎 Web Search Results:
1. Quantum Computing Basics - https://example.com
2. Latest Research on Quantum Computing - https://example.com

## Project Structure
QA_AGENT/
│── app.py          # Main application script (runs the agent)
│── agent.py        # Defines the agent's behavior
│── requirements.txt # Dependencies
│── env.example     # Example environment variables file
│── tools/          # Directory for agent's tools
│   ├── llm_tool.py  # LLM-powered question-answering tool
│   ├── web_search.py # Hugging Face-based web search tool
│   ├── utils.py     # Helper functions (logging, formatting, etc.)
│── config.py       # Configuration settings
│── README.md       # Project documentation
