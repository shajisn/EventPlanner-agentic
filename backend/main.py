from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Define a model for the request body
class Query(BaseModel):
    question: str

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Event Planner API"}

@app.post("/ask")
async def ask_question(query: Query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query.question,
            max_tokens=150
        )
        return {"answer": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
