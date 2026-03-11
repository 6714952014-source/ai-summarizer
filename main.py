from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

summarizer = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

class Text(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Summarizer Running"}

@app.post("/summarize")
def summarize(data: Text):

    prompt = f"Summarize this text: {data.text}"

    result = summarizer(
        prompt,
        max_length=100,
        do_sample=False
    )

    return {"summary": result[0]["generated_text"]}