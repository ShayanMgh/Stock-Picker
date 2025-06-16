#!/usr/bin/env python
import sys, warnings, json, datetime, os
from stock_picker.crew import StockPicker
from stock_picker.utils.serper import fetch_trending_news

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():
    sector = os.getenv("SECTOR", "technology")       # default sector
    fresh_news = fetch_trending_news(sector)         # <-- live data

    inputs = {
        "sector": sector,
        "current_year": str(datetime.datetime.now().year),
        "news_snippets": fresh_news                  # inject into crew
    }

    try:
        result = StockPicker().crew().kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        raise Exception(f"Crew run failed: {e}")

# ------------------------------------------------------------------
# (train / replay / test helpers unchanged – show only run() here)
if __name__ == "__main__":
    run()
