import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that rewrites text to make it clearer and simpler."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# Example use
user_input = input("Enter text to rewrite:\n")
print("\nRewritten text:\n", rewrite_text(user_input))
