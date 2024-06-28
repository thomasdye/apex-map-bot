import requests
import time
import json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
import pytz

# Load environment variables from .env file
load_dotenv()

# Retrieve the webhook URL and API key from environment variables
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
API_KEY = os.getenv('API_KEY')

# Apex Legends Map Rotation API URL
API_URL = f'https://api.mozambiquehe.re/maprotation?auth={API_KEY}'

# Store the message ID to edit the message
message_id = None

def fetch_map_rotation():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def format_remaining_time(seconds):
    remaining_time = timedelta(seconds=seconds)
    return str(remaining_time)

def format_discord_message(data):
    current = data['current']
    next_map = data['next']
    
    # Get current time in UTC and convert to EST
    utc_now = datetime.now(timezone.utc)
    est = pytz.timezone('US/Eastern')
    est_now = utc_now.astimezone(est)
    timestamp = est_now.strftime('%m/%d at %H:%M %p EST')

    message = {
        "content": f"Last Updated: {timestamp}",
        "embeds": [
            {
                "title": "Current Map",
                "description": f"**{current['map']}**\n"
                               f"**Remaining Time:** {format_remaining_time(current['remainingSecs'])}\n",
                "image": {"url": current['asset']},
                "color": 3447003
            },
            {
                "title": "Next Map",
                "description": f"**{next_map['map']}**\n"
                               f"**Starts In:** {format_remaining_time(current['remainingSecs'])}\n"
                               f"**Duration:** {format_remaining_time(next_map['DurationInSecs'])}\n",
                "color": 15105570
            }
        ]
    }
    return message

def post_to_discord(message):
    global message_id
    headers = {"Content-Type": "application/json"}

    if message_id is None:
        response = requests.post(f"{DISCORD_WEBHOOK_URL}?wait=true", data=json.dumps(message), headers=headers)
        if response.status_code == 200:
            print("Successfully posted to Discord")
            response_data = response.json()
            message_id = response_data['id']  # Store the message ID
        else:
            print(f"Failed to post to Discord: {response.status_code}")
    else:
        # Edit the existing message
        webhook_url = f"{DISCORD_WEBHOOK_URL}/messages/{message_id}"
        response = requests.patch(webhook_url, data=json.dumps(message), headers=headers)
        if response.status_code == 200:
            print("Successfully updated Discord message")
        else:
            print(f"Failed to update Discord message: {response.status_code}")

def main():
    while True:
        data = fetch_map_rotation()
        if data:
            message = format_discord_message(data)
            post_to_discord(message)
        time.sleep(600)  # Wait for 10 minutes before fetching again

if __name__ == "__main__":
    main()
