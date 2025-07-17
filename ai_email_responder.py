import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(incoming_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a polite and professional customer service assistant. Draft a friendly reply to the customer's message."},
            {"role": "user", "content": incoming_message}
        ]
    )
    return response.choices[0].message.content


# Example use
incoming = input("Paste the customer's message:\n")
print("\nSuggested reply:\n", generate_reply(incoming))
