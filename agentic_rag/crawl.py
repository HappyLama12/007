import requests
from config import CRAWL4AI_URL, TARGET_URLS

def crawl():
    all_text = []
    for url in TARGET_URLS:
        response = requests.post(f"{CRAWL4AI_URL}/crawl", json={"url": url})
        if response.ok:
            text = response.json().get("text", "")
            all_text.append(text)
    return all_text
