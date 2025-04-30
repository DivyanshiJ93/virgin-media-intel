# article_parser.py

from newspaper import Article
import requests

def extract_article_text(url):
    """
    Extracts main content from a URL using newspaper3k.
    Args:
        url (str): The webpage URL.
    Returns:
        Tuple: (title, clean_text) or (None, None) if failed.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            raise ValueError("Article has no text")

        return article.title, article.text.strip()

    except Exception as e:
        print(f"[WARN] Could not parse article at {url} — {e}")
        return None, None
