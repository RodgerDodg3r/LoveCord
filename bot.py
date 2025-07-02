import discord
from discord.ext import commands
from dotenv import load_dotenv

from functions.guild_handler import guild_sync_config_with_template

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
        guild_sync_config_with_template(guild.id)
    
    for file in os.listdir('./cogs/'):
        if (not file.endswith('.py')):
            continue
    
        cog_name = file[:-3]
        try:
            await bot.load_extension(f'cogs.{cog_name}')
            print(f"Loaded cog: {cog_name}")
        
        except Exception as error:
            print(f"An error accoured while loading {cog_name}: {error}") 

if __name__ == "__main__":
    bot.run(token)