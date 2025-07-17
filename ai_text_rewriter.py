from dotenv import load_dotenv
import os
import openai

load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional text rewriter. Make the text clearer and cleaner."},
            {"role": "user", "content": text}
        ]
    )
    return response["choices"][0]["message"]["content"]

user_input = input("Enter text to rewrite: ")
print("Rewritten text:\n", rewrite_text(user_input))
