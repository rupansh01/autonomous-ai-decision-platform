import os
import json
from openai import OpenAI

# -------------------------------------------------
# OpenAI Client
# -------------------------------------------------
# IMPORTANT:
# API key MUST be set as environment variable:
# export OPENAI_API_KEY="sk-xxxx"
# -------------------------------------------------

client = OpenAI()

# -------------------------------------------------
# System Prompt (STRICT)
# -------------------------------------------------
SYSTEM_PROMPT = """
You are a customer support analyst working for a large company.

Your task:
- Analyze the customer complaint
- Estimate severity on a scale of 1 to 10
- Explain reasoning briefly
- Suggest an action

STRICT RULES:
1. Respond ONLY in valid JSON
2. Do NOT add extra text
3. Severity must be an integer between 1 and 10

JSON FORMAT:
{
  "severity": 0,
  "reasoning": "string",
  "suggested_action": "string"
}
"""

# -------------------------------------------------
# Core Function
# -------------------------------------------------
def analyze_complaint(complaint_text: str):
    """
    Uses OpenAI to analyze a customer complaint
    and returns structured reasoning.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": complaint_text}
            ],
            temperature=0.2,
            max_tokens=200
        )

        content = response.choices[0].message.content.strip()

        # Try parsing JSON strictly
        parsed = json.loads(content)

        # Basic validation
        if (
            "severity" not in parsed or
            "reasoning" not in parsed or
            "suggested_action" not in parsed
        ):
            raise ValueError("Invalid JSON structure from OpenAI")

        return parsed

    except Exception as e:
        # SAFE FALLBACK (never break system)
        return {
            "severity": 5,
            "reasoning": f"LLM analysis failed, fallback used. Error: {str(e)}",
            "suggested_action": "ESCALATE"
        }
