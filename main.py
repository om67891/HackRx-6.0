# main.py

from ImprovedPolicyQA import ImprovedPolicyQA
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
qa_system = ImprovedPolicyQA()

# ⚠️ Update this with the correct path to your real PDF
PDF_PATH = "C:/Users/spyte/Documents/nlp_notes.pdf"

class QuestionRequest(BaseModel):
    questions: List[str]

@app.post("/ask/")
def ask_questions(request: QuestionRequest):
    try:
        answers = qa_system.run(PDF_PATH, request.questions)
        return {"answers": answers}
    except Exception as e:
        return {"error": str(e)}
    
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Render!"}

# 👇 Add this block at the bottom of main.py
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))  # Render will inject PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

