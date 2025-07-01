from fastapi import FastAPI
app = FastAPI()

@app.get("/ask")
def ask(question: str):
    return {"answer": f"Вы спросили: {question}"}