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
