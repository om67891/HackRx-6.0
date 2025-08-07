from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import uvicorn

from ImprovedPolicyQA import ImprovedPolicyQA

app = FastAPI()
qa_system = ImprovedPolicyQA()

# Make sure this PDF is in your project directory on Render
PDF_PATH = "./nlp_notes.pdf"  # ✅ Use relative path, not Windows path

class QuestionRequest(BaseModel):
    questions: List[str]

@app.post("/ask/")
def ask_questions(request: QuestionRequest):
    try:
        answers = qa_system.run(PDF_PATH, request.questions)
        return {"answers": answers}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Render!"}

# 👇 Main entry point
if __name__ == "__main__":
    # Safely get the port from environment, fallback to 8000
    port_str = os.environ.get("PORT")
    port = int(port_str) if port_str and port_str.isdigit() else 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
