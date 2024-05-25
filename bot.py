import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the bot token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='addclip')
async def add_clip(ctx, url: str, timestamp: str, *, description: str):
    if ctx.channel.name != 'clip-suggestions':
        await ctx.send("Please use the `clip-suggestions` channel for adding clip suggestions.")
        return

    channel = discord.utils.get(ctx.guild.text_channels, name='clip-suggestions')
    if channel:
        embed = discord.Embed(title="New Clip Suggestion", color=discord.Color.blue())
        embed.add_field(name="URL", value=url, inline=False)
        embed.add_field(name="Timestamp", value=timestamp, inline=True)
        embed.add_field(name="Description", value=description, inline=True)
        embed.set_footer(text=f"Suggested by {ctx.author}")
        await channel.send(embed=embed)
        await ctx.send("Clip suggestion added!")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'clip-suggestions' not found!")

@bot.command(name='listclips')
async def list_clips(ctx):
    if ctx.channel.name != 'clip-suggestions':
        await ctx.send("Please use the `clip-suggestions` channel for listing clip suggestions.")
        return

    channel = discord.utils.get(ctx.guild.text_channels, name='clip-suggestions')
    if channel:
        messages = await channel.history(limit=100).flatten()
        if messages:
            embed = discord.Embed(title="Clip Suggestions", color=discord.Color.green())
            for msg in messages:
                if msg.embeds:
                    embed.add_field(name=msg.embeds[0].fields[1].value, value=msg.embeds[0].fields[2].value, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No clip suggestions found.")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'clip-suggestions' not found!")

bot.run(TOKEN)
