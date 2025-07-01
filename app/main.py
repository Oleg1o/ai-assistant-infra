from fastapi import FastAPI, Request
from langchain_community.llms import Ollama

app = FastAPI()

llm = Ollama(model="llama3")

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    response = llm.invoke(question)

    return {"answer": response}
@app.get("/ask")
def ask(question: str):
    return {"answer": f"Вы спросили: {question}"}