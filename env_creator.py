import os

def create_env_file():
    api_key = input("Please enter your Apex Legends API key: ")
    discord_webhook_url = input("Please enter your Discord webhook URL: ")

    with open(".env", "w") as env_file:
        env_file.write(f"API_KEY={api_key}\n")
        env_file.write(f"DISCORD_WEBHOOK_URL={discord_webhook_url}\n")

    print(".env file created successfully!")

if __name__ == "__main__":
    create_env_file()
