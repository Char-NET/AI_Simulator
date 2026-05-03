import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def call_llm(prompt):

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an AI debate agent. "
                    "You are part of an ongoing conversation. "
                    "NEVER restart the topic, NEVER repeat introductions, "
                    "and NEVER reset the discussion. "
                    "Respond directly to the last message."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return f"[ERROR]: {response.text}"