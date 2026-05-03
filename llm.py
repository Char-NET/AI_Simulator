import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def call_llm(prompt):

 
    if not GROQ_API_KEY:
        return "[ERROR]: Missing GROQ_API_KEY in environment variables"

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are in a live debate. "
                    "Keep responses under 120 words. "
                    "Be direct and concise. "
                    "Do NOT repeat yourself or restart the topic."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"[ERROR]: {str(e)}"
