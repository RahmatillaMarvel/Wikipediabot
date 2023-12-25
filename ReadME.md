# Telegram Wikipedia Bot

## Overview
This is a simple Telegram bot that utilizes the Aiogram library and the Wikipedia API to provide Wikipedia summaries in the Uzbek language.

## Getting Started
To get started with this bot, follow the steps below:

### Prerequisites
- Python 3.6 or later
- Aiogram library (2.25 version)
- Wikipedia API library

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/RahmatillaMarvel/Wikipediabot.git
   cd Wikipediabot

### Install libraries
1. Install the required dependencies:
``` pip install -r requirements.txt```
2. Obtain a Telegram Bot Token:

Create a new bot on Telegram by talking to the BotFather.
Copy the generated API token.

Configure the Bot Token:

Open the config.py file.
Replace 'BOT_TOKEN' with the Telegram Bot Token you obtained.

### Usage
Run the bot using the following command:
```python tgbot.py```
### Bot Commands
/start: Displays a welcome message.
Sending any other message triggers a search on Wikipedia. The bot responds with a summary of the relevant article in Uzbek.
### Configuration
You can configure the bot's language and other settings in the config.py file.

### Issues and Contributions
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
