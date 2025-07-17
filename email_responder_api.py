from fastapi import FastAPI, Form
from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.post("/generate-reply/")
def generate_reply(message: str = Form(...)):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a polite and professional customer service assistant. Draft a friendly reply to the customer's message."},
            {"role": "user", "content": message}
        ]
    )
    return {"reply": response.choices[0].message.content}
