from langchain.llms import Ollama

llm = Ollama(model="llama3")

def get_llm_response(prompt: str) -> str:
    return llm(prompt)