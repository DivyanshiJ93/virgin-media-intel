# main.py

# main.py

import os
import sys
import json


# Ensure root directory is in Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from competitors import get_infosys_competitors
from search_engine import search_google_serpapi
from article_parser import extract_article_text
from analyzer import analyze_text_llm
from config.config import QUERY_TEMPLATE, NUM_RESULTS


RESULTS_PATH = "data/results.json"

def run_intel():
    final_results = []

    competitors = get_infosys_competitors()
    print(f"🔍 Running analysis for {len(competitors)} competitors...\n")

    for comp in competitors:
        query = QUERY_TEMPLATE.format(competitor=comp)
        print(f"🔎 Searching for: {comp} ...")

        urls = search_google_serpapi(query, num_results=NUM_RESULTS)
        print(f"🔗 Found {len(urls)} URLs for {comp}")

        for url in urls:
            print(f"📰 Processing: {url}")
            title, text = extract_article_text(url)

            if not title or not text:
                continue

            confirmed, reason = analyze_text_llm(comp, title, text)
            if confirmed:
                print(f"✅ Confirmed: {comp} has worked with Virgin Media → {title}")
                final_results.append({
                    "competitor": comp,
                    "title": title,
                    "url": url,
                    "summary": reason
                })
            else:
                print(f"⛔ Not confirmed: {comp} → {title} — Reason: {reason}")

    print("\n✅ Finished scanning. Writing results...")

    os.makedirs("data", exist_ok=True)
    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(final_results, f, indent=2, ensure_ascii=False)

    print(f"📁 Results saved to {RESULTS_PATH}")
    return final_results


if __name__ == "__main__":
    run_intel()
