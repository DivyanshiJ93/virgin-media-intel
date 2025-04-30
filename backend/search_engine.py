# search_engine.py

import requests
import time
from config.config import SERPAPI_KEY

def search_google_serpapi(query, num_results=5):
    """
    Searches Google using SerpAPI.
    Args:
        query (str): The search term.
        num_results (int): How many top links to return.
    Returns:
        List of result URLs.
    """
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key":SERPAPI_KEY,
        "engine": "google",
        "num": num_results
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        results = []
        for res in data.get("organic_results", []):
            link = res.get("link")
            if link and link.startswith("http"):
                results.append(link)

        return results

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Search failed for query: {query} — {e}")
        return []
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return []
