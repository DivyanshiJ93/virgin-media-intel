# analyzer.py

import openai
from config.config import OPENAI_KEY

# Initialize key (safe even if empty)
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY

def analyze_text_llm(competitor, article_title, article_text):
    """
    Uses GPT to detect whether an article confirms collaboration.
    Returns a tuple: (bool, reason)
    """
    if not OPENAI_KEY:
        return analyze_text_rule_based(competitor, article_title, article_text)

    try:
        prompt = f"""
You are a research assistant. Determine if the article below indicates that {competitor} has worked with Virgin Media in any capacity (e.g. partnership, client relationship, IT services, outsourcing, etc).

Respond with YES or NO, and briefly explain why.

TITLE: {article_title}
CONTENT: {article_text[:3000]}
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

        answer = response.choices[0].message.content.strip().lower()
        if "yes" in answer:
            return True, answer
        else:
            return False, answer

    except Exception as e:
        print(f"[WARN] LLM analysis failed, using fallback. {e}")
        return analyze_text_rule_based(competitor, article_title, article_text)


def analyze_text_rule_based(competitor, title, text):
    """
    Simple rule-based keyword check as fallback.
    """
    keywords = ["partnership", "client", "project", "contract", "worked with", "collaboration", "delivered"]
    if competitor.lower() in text.lower() and any(k in text.lower() for k in keywords):
        reason = f"Matched keywords indicating {competitor} worked with Virgin Media."
        return True, reason
    return False, "No strong match for keywords or competitor name."
