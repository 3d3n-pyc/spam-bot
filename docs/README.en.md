# Utils Bot

A simple Discord bot using [discord.py](https://discordpy.readthedocs.io/) that provides a `/spam` command to send a message multiple times via a button.

> [!CAUTION]
> I am not responsible for any actions taken using this bot.
> I am not responsible for any ban resulting from the use of this bot.

## Features

- `/spam` slash command: Send a message up to 5 times per button click.
- Button-based UI for easy spamming.
- Message length and amount validation.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/3d3n-pyc/spam-bot.git
   cd spam-bot
   ```

2. **Install dependencies:**
   ```sh
   pip install discord.py python-dotenv
   ```

3. **Create a `.env` file:**
   ```
   BOT_TOKEN=your-bot-token-here
   ```

4. **Run the bot:**
   ```sh
   python main.py
   ```

## Usage

- Use `/spam` in your Discord server.
- Enter your message and the amount (1-5).
- Click the 📩 button to send your message multiple times.

## Notes

- Make sure your bot has the necessary permissions for slash commands and message sending.
- The bot only allows messages up to 2000 characters and up to 5 repeats per click.

## License

MIT
