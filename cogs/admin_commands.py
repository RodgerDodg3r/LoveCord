import discord
from discord.ext import commands
from discord import app_commands

from functions.guild_handler import *


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "setbotchannel")
    @commands.has_permissions(manage_messages=True)
    async def set_bot_channel_command(self, ctx):

        channel_id = ctx.channel.id
        guild_data = guild_get_data(ctx.guild.id)
        guild_data["bot_channel"] = channel_id

        guild_save_data(ctx.guild.id, guild_data)


        await ctx.send(f"✅ Channel {ctx.channel.mention} is a default LoveCord's channel")

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))

