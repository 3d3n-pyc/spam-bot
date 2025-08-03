import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import asyncio
import sys
import logging

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logger = logging.getLogger("main")

class Embed:
    @staticmethod
    def error(title: str, description: str):
        embed = discord.Embed(title=title, description=description, color=discord.Color.red())
        embed.timestamp = discord.utils.utcnow()
        return embed

    @staticmethod
    def success(title: str, description: str):
        embed = discord.Embed(title=title, description=description, color=discord.Color.green())
        embed.timestamp = discord.utils.utcnow()
        return embed
    
    @staticmethod
    def info(title: str, description: str):
        embed = discord.Embed(title=title, description=description, color=discord.Color.blurple())
        embed.timestamp = discord.utils.utcnow()
        return embed

class SpamButton(discord.ui.View):
    def __init__(self, message: str, amount: int):
        super().__init__(timeout=None)
        self.message = message
        self.amount = amount

    @discord.ui.button(emoji='📩', style=discord.ButtonStyle.primary)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            embed=Embed.info(
                "Spam Message",
                "Spamming your message..."
            ),
            ephemeral=True
        )
        for _ in range(self.amount):
            await interaction.followup.send(self.message, ephemeral=False)

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="spam", description="Send a message multiple times.")
    @app_commands.describe(message="The message to send", amount="Number of times for each button click (default: 5)")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.user_install()
    async def spam(self, interaction: discord.Interaction, message: str, amount: int = 5):
        await interaction.response.defer(ephemeral=True)

        if not (1 <= amount <= 5):
            return await interaction.followup.send(
                embed=Embed.error(
                    "Invalid Amount",
                    "Please specify an amount between 1 and 5."
                ),
                ephemeral=True
            )

        if len(message) > 2000:
            return await interaction.followup.send(
                embed=Embed.error(
                    "Message Too Long",
                    "Your message is too long. Please keep it under 2000 characters."
                ),
                ephemeral=True
            )

        await interaction.followup.send(
            embed=Embed.info(
                "Spam Message",
                "Click the button below to spam your message."
            ),
            view=SpamButton(message, amount),
            ephemeral=True
        )

if __name__ == "__main__":
    load_dotenv()

    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        discord.utils.setup_logging()
        logger.info(f"Logged in as {bot.user}")
        logger.info(f"Link to invite: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}")

        await bot.add_cog(Spam(bot))
        await bot.tree.sync()
    
    bot_token = os.getenv("BOT_TOKEN")
    bot.run(bot_token)
