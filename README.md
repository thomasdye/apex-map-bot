
# Apex Legends Map Rotation Bot

This project fetches the current and upcoming map rotations for Apex Legends and posts the information to a Discord channel via a webhook. The project requires an Apex Legends API key and a Discord webhook URL.

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

### Installing Python and pip

#### Windows

1. Download the Python installer from the [official Python website](https://www.python.org/downloads/windows/).
2. Run the installer and ensure that the "Add Python to PATH" option is checked.
3. Follow the installation instructions.
4. Open Command Prompt and verify the installation by running:

    ```sh
    python --version
    pip --version
    ```

#### macOS

1. Open Terminal.
2. Install Homebrew if you don't have it already by running:

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Install Python by running:

    ```sh
    brew install python
    ```

4. Verify the installation by running:

    ```sh
    python3 --version
    pip3 --version
    ```

#### Linux

1. Open Terminal.
2. Use your package manager to install Python. For example, on Debian-based distributions (like Ubuntu), run:

    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```

3. Verify the installation by running:

    ```sh
    python3 --version
    pip3 --version
    ```

### Project Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:

    ```sh
    pip install requests python-dotenv pytz
    ```

## Setup

### Apex Legends API Key

You need to obtain an Apex Legends API key. Follow these steps:

1. Go to the [Apex Legends API website](https://apexlegendsapi.com).
2. Sign up for an account or log in if you already have one.
3. Navigate to the API key section and generate a new API key.
4. Copy the generated API key.

### Discord Webhook URL

To create a Discord webhook, follow these steps:

1. Open Discord and navigate to the server where you want to post the map rotation updates.
2. Click on the server name at the top of the channel list to open the server settings.
3. Go to the "Integrations" section.
4. Click on "Create Webhook".
5. Give the webhook a name and select the channel where you want the messages to be posted.
6. Click on "Copy Webhook URL" to copy the webhook URL to your clipboard.

### Environment Variables

Create a `.env` file in the project directory and add the following lines, replacing `YOUR_API_KEY` and `YOUR_DISCORD_WEBHOOK_URL` with your actual API key and webhook URL:

```env
API_KEY=YOUR_API_KEY
DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
```

Alternatively, you can use the provided `env_creator.py` script to create the `.env` file:

1. Run the script:

    ```sh
    python env_creator.py
    ```

2. Follow the prompts to enter your API key and Discord webhook URL. The script will create the `.env` file for you.

## Running the Bot

To run the bot, execute the following command:

```sh
python apex_map_bot.py
```

The bot will fetch the current and upcoming map rotations for Apex Legends and post the information to the specified Discord channel every 10 minutes.
