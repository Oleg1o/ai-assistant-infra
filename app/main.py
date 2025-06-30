from fastapi import FastAPI, Query
from chain import get_llm_response

app = FastAPI()

@app.get("/ask")
async def ask(question: str = Query(..., description="Ваш вопрос")):
    response = get_llm_response(question)
    return {"answer": response}