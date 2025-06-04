
from tools.llm_tools import LLMTool

def main():
    llm_tool = LLMTool()
    print("Welcome to your AI Agent! Type 'exit' to quit.")

    while True:
        query = input("\nAsk a question: ")
        if query.lower() == "exit":
            break

        response = llm_tool.handle_query(query)
        
        print("\nAI Answer:", response["AI Answer"])
        print("\n🔎 Web Search Results:")
        print(response["Web Sources"])

if __name__ == "__main__":
    main()