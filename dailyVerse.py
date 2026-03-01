import requests
import schedule
import time
import os

WEBHOOK_URL = os.getenv("STOAT_WEBHOOK_URL")
OURMANNA_URL = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"

def post_daily_verse():
    try:
        # 1. Fetch from OurManna
        response = requests.get(OURMANNA_URL, headers={'accept': 'application/json'})
        response.raise_for_status()
        data = response.json()
        
        # 2. Extract specific OurManna fields
        details = data['verse']['details']
        text = details['text']
        reference = details['reference']
        version = details['version']

        # 3. Format for Stoat
        payload = {
            "content": f"**Daily Manna**\n\n\"{text}\"\n— *{reference} ({version})*"
        }

        # 4. Post to Stoat
        requests.post(WEBHOOK_URL, json=payload)
        print(f"Posted: {reference}")
        
    except Exception as e:
        print(f"Error: {e}")

# Set the schedule for 5:00 AM
schedule.every().day.at("05:00").do(post_daily_verse)

if __name__ == "__main__":
    if not WEBHOOK_URL:
        print("FATAL ERROR: STOAT_WEBHOOK_URL environment variable is missing!")
    else:
        print("Daily Verse started. Schedule set for 05:00 AM daily.")
        # Optional: Uncomment the line below to post one immediately on startup
        # post_daily_verse() 
        
        while True:
            schedule.run_pending()
            time.sleep(60) # Check every minute if it's 5am yet