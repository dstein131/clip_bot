import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

# Load environment variables from a .env file
load_dotenv()

# Get the bot token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not TOKEN:
    raise ValueError("No token provided. Set the DISCORD_BOT_TOKEN environment variable.")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Fun Feature: Kek
@bot.command(name='kek')
async def kek(ctx):
    if ctx.author.name != 'sirvosef':
        await ctx.send("You don't have permission to use this command.")
        return

    try:
        print(f'!kek command received in channel: {ctx.channel} by user: {ctx.author}')
        memes = [
            "https://imgur.com/gallery/every-morrissey-song-uXxI3Zr#/t/morrissey",
            "https://imgur.com/gallery/morrisseys-dying-hyqtZ92#/t/morrissey",
            "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwitter.com%2Fbucktickzone%2Fstatus%2F563749346953285632&psig=AOvVaw1qEP_yGDEaX4QjlD4OpEna&ust=1716744475174000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIj569apqYYDFQAAAAAdAAAAABAE".
            "https://www.thepinknews.com/wp-content/uploads/2021/04/Morrissey.jpg",
        ]
        selected_meme = random.choice(memes)
        print(f'Sending meme: {selected_meme}')
        await ctx.send(selected_meme)
    except Exception as e:
        print(f'Error in !kek command: {e}')
        await ctx.send("An error occurred while processing the command.")

# Respond to regalsalvatore
@bot.event
async def on_message(message):
    if message.author.name == 'regalsalvatore' and not message.author.bot:
        await message.channel.send('jajajajaja')
    await bot.process_commands(message)

# Error Handling
@bot.event
async def on_command_error(ctx, error):
    print(f'Error: {error}')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        await ctx.send("An error occurred.")
        raise error

# Run the bot
bot.run(TOKEN)
