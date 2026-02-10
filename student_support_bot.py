import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"

conversation_context = """
You are an AI-Powered Student Support Chatbot.

You help students with:
- Course information
- Admission guidance
- Eligibility
- Exams
- Career advice

Use simple English and polite tone.
"""

def student_support_bot(user_input, history={}):

    if "conversation" not in history:
        history["conversation"] = [
            {"role": "system", "content": conversation_context}
        ]

    history["conversation"].append({
        "role": "user",
        "content": user_input
    })

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": history["conversation"],
        "temperature": 0.6
    }

    try:
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        if "choices" not in result:
            return f"API Error: {result}"

        reply = result["choices"][0]["message"]["content"]

        history["conversation"].append({
            "role": "assistant",
            "content": reply
        })

        return reply

    except Exception:
        return "Server error. Please try again."
