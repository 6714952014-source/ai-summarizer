from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

class Text(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Summarizer Running"}

@app.post("/summarize")
def summarize(data: Text):

    payload = {
        "inputs": data.text
    }

    response = requests.post(API_URL, json=payload)
    result = response.json()

    return {"summary": result[0]["summary_text"]}