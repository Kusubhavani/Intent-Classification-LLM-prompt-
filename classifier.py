import json
import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_intent(message: str):
    prompt = f"""
Classify the user's intent.
Possible intents: code, data, writing, career, unclear

Respond ONLY with JSON like this:
{{ "intent": "code", "confidence": 0.95 }}

User message:
{message}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content
        json_match = re.search(r"\{.*\}", result, re.DOTALL)

        if json_match:
            parsed = json.loads(json_match.group())
            return parsed
        else:
            return {"intent": "unclear", "confidence": 0.0}

    except Exception as e:
        print("Classifier error:", e)
        return {"intent": "unclear", "confidence": 0.0}