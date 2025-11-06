#Ollama.py
import json
import re

import requests


def extract_json(text):
    json_match = re.search(r'\{.*?\}', text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            return {"intent": "error", "sentiment": "error", "summary": "JSON decoding error"}
    return {"intent": "error", "sentiment": "error", "summary": "No JSON found"}

def analyze_with_ollama(text, model="llama3"):
    allowed_intents = [
        "accommodation_complaint", "account_inquiry", "appointment_management",
        "billing_complaint", "booking_complaint", "business_inquiry",
        "community_feedback", "complaint", "customer_experience",
        "delivery_status", "educational_feedback", "entertainment_review",
        "environment_complaint", "event_review", "express_appreciation",
        "express_gratitude", "express_opinion", "express_praise",
        "express_satisfaction", "facility_feedback", "financial_complaint",
        "financial_inquiry", "food_review", "health_complaint", "health_inquiry",
        "healthcare_feedback", "job_inquiry", "location_inquiry", "order_inquiry",
        "payment_inquiry", "policy_complaint", "policy_feedback", "policy_inquiry",
        "procedural_inquiry", "process_complaint", "product_complaint",
        "product_feedback", "product_inquiry", "rewards_feedback",
        "schedule_inquiry", "service_complaint", "service_feedback",
        "service_inquiry", "service_review", "shipping_inquiry",
        "technical_complaint", "technical_feedback", "technical_support",
        "transportation_complaint", "travel_complaint", "travel_review",
        "warranty_inquiry"
    ]

    prompt = f"""
You are an NLP assistant. Analyze the following user input and return a JSON object:

- "intent": Must be one of: {allowed_intents}
- "sentiment": One word — "positive", "neutral", or "negative".
- "summary": A short plain-English summary of the input.

Text: "{text}"

Respond ONLY with a JSON object:
{{ "intent": "...", "sentiment": "...", "summary": "..." }}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        return extract_json(response.json()["response"])
    except Exception as e:
        return {"intent": "error", "sentiment": "error", "summary": str(e)}

def generate_chatbot_response(transcript, model="llama3"):
    prompt = f"""
You're a friendly multilingual assistant. Reply naturally to the user's message.

User: "{transcript}"

Your response should:
- Be conversational and helpful.
- Be at least 2 lines and at most 6 lines.
- Use natural sentence structure (avoid being too brief or too lengthy).

Respond:
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Sorry, I couldn't respond due to an error: {e}"
