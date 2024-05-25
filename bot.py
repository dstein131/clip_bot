import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random



# Get the bot token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Fun Feature: Kek
@bot.command(name='kek')
async def kek(ctx):
    memes = [
        "https://i.imgur.com/w3duR07.png",
        "https://i.imgur.com/2vQtZBb.png",
        "https://i.imgur.com/AfFp7pu.png"
    ]
    await ctx.send(random.choice(memes))

# Error Handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        await ctx.send("An error occurred.")
        raise error

# Automatically generated help command is included by default
bot.run(TOKEN)
