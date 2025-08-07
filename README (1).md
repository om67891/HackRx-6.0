# 🛡️ Improved Policy QA - FastAPI

This is a FastAPI-based backend for answering insurance policy questions based on uploaded or linked PDF documents.

---

## 🚀 Run the FastAPI App

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the FastAPI server
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

FastAPI interactive docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 Sample cURL Request

```bash
curl -X POST http://localhost:8000/ask/ ^
  -H "Authorization: Bearer hackrx-secret-token" ^
  -H "Content-Type: application/json" ^
  -d "{ \"documents\": \"http://example.com/sample.pdf\", \"questions\": [\"What is the premium?\", \"Who is covered?\"] }"
```

📝 **Note**:
- On Linux/Mac, replace `^` with `\` for line continuation.
- Replace the URL and questions as needed.

---

## 🔐 Authorization

Add the following header to authenticate:

```
Authorization: Bearer hackrx-secret-token
```

---