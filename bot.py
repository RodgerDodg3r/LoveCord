import discord
from discord.ext import commands
from dotenv import load_dotenv

import os

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
@bot.event
async def on_ready():
    print(f"💖 Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game("Loving someone deeply <3"))

    for guild in bot.guilds:
        print(f"Loaded on {guild.name}")


if __name__ == "__main__":
    bot.run(token)