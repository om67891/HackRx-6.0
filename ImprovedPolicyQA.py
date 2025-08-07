# ImprovedPolicyQA.py

import fitz  # PyMuPDF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ImprovedPolicyQA:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def extract_text(self, file_path):
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text

    def split_paragraphs(self, text):
        paragraphs = re.split(r'\n\s*\n', text)  # split on empty lines
        cleaned_paragraphs = [p.strip().replace('\n', ' ') for p in paragraphs if len(p.strip()) > 30]
        return cleaned_paragraphs

    def find_best_match(self, question, paragraphs):
        corpus = paragraphs + [question]
        tfidf = self.vectorizer.fit_transform(corpus)
        cosine_similarities = cosine_similarity(tfidf[-1], tfidf[:-1])
        best_idx = cosine_similarities.argmax()
        best_score = cosine_similarities[0][best_idx]
        if best_score < 0.1:
            return "Sorry, no relevant information found."
        return paragraphs[best_idx]

    def run(self, file_path, questions):
        pdf_text = self.extract_text(file_path)
        paragraphs = self.split_paragraphs(pdf_text)
        answers = []

        for question in questions:
            best_para = self.find_best_match(question, paragraphs)
            answers.append(f"{best_para.strip()}")

        return answers
