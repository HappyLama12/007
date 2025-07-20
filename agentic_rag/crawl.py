import requests
import time
from config import CRAWL4AI_URL, WEBSITE_URL

def crawl_website(url=WEBSITE_URL, depth=2):
    payload = {
        "urls": [url],
        "depth": depth,
        "crawl_subdomains": True,
        "options": {"download_assets": False}
    }

    headers = {"Content-Type": "application/json"}

    resp = requests.post(f"{CRAWL4AI_URL}/crawl", json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    if "id" in data:
        crawl_id = data["id"]
        print(f"[INFO] Crawl started: ID = {crawl_id}")
        while True:
            status = requests.get(f"{CRAWL4AI_URL}/crawl/{crawl_id}").json()
            if status["status"] == "done":
                print("[INFO] Crawl completed.")
                return status["results"]
            elif status["status"] == "error":
                raise Exception(f"Crawl failed: {status}")
            else:
                print("[INFO] Crawling... waiting...")
                time.sleep(5)
    elif "results" in data:
        print("[INFO] Crawl completed immediately.")
        return data["results"]
    else:
        raise Exception(f"[ERROR] Unexpected crawl response: {data}")
