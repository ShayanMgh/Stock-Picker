# src/stock_picker/utils/serper.py
import os, requests, datetime
from typing import List, Dict

SERPER_ENDPOINT = "https://google.serper.dev/news"

def fetch_trending_news(sector: str, n: int = 10) -> List[Dict]:
    """
    Return the latest N news items for a sector using Serper.dev.
    Expects SERPER_API_KEY in the environment.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise EnvironmentError("SERPER_API_KEY not set in .env")

    payload = {"q": f"{sector} companies", "num": n}
    resp = requests.post(SERPER_ENDPOINT, json=payload,
                         headers={"X-API-KEY": api_key}, timeout=20)
    resp.raise_for_status()
    news_items = resp.json().get("news", [])
    # keep only the fields we need
    clean = [{
        "title": item["title"],
        "link": item["link"],
        "snippet": item["snippet"],
        "date": item.get("date") or str(datetime.date.today())
    } for item in news_items]
    return clean
