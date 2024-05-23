import discord
from discord.ext import commands
from googleapiclient.discovery import build
import re

# YouTube Data API key
YOUTUBE_API_KEY = 'AIzaSyCRO6LdrRE0hdjHFXblMZZFHNN_3-4lpYU'

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to extract video ID from URL
def extract_video_id(url):
    video_id = None
    # Common YouTube URL patterns
    patterns = [
        r'(?<=v=)[^&#]+', # ...?v=VIDEO_ID
        r'(?<=be/)[^&#]+', # ...be/VIDEO_ID
        r'(?<=embed/)[^&#]+', # ...embed/VIDEO_ID
        r'(?<=youtu.be/)[^&#]+' # ...youtu.be/VIDEO_ID
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group()
            break
    return video_id

# Function to get video details
def get_video_details(video_id):
    response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    if response['items']:
        video = response['items'][0]
        title = video['snippet']['title']
        channel_title = video['snippet']['channelTitle']
        return title, channel_title
    return None, None

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Command to add a clip suggestion
@bot.command(name='addclip')
async def add_clip(ctx, url: str, timestamp: str, *, description: str):
    # Post the suggestion in the 'clip-suggestions' channel
    channel = discord.utils.get(ctx.guild.text_channels, name='clip-suggestions')
    if channel:
        video_id = extract_video_id(url)
        if video_id:
            title, channel_title = get_video_details(video_id)
            if title and channel_title:
                embed = discord.Embed(title="New Clip Suggestion", color=discord.Color.blue())
                embed.add_field(name="Video Title", value=title, inline=False)
                embed.add_field(name="Channel", value=channel_title, inline=False)
                embed.add_field(name="Timestamp", value=timestamp, inline=True)
                embed.add_field(name="Description", value=description, inline=True)
                embed.add_field(name="URL", value=url, inline=False)
                embed.set_footer(text=f"Suggested by {ctx.author}")
                await channel.send(embed=embed)
                await ctx.send("Clip suggestion added in the `clip-suggestions` channel!")
            else:
                await ctx.send("Could not retrieve video details. Please check the URL.")
        else:
            await ctx.send("Invalid YouTube URL.")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'clip-suggestions' not found!")

# Command to list all clip suggestions
@bot.command(name='listclips')
async def list_clips(ctx):
    # Post the list of suggestions in the channel where the command was invoked
    channel = discord.utils.get(ctx.guild.text_channels, name='clip-suggestions')
    if channel:
        messages = await channel.history(limit=100).flatten()
        if messages:
            embed = discord.Embed(title="Clip Suggestions", color=discord.Color.green())
            for msg in messages:
                if msg.embeds:
                    embed.add_field(name=msg.embeds[0].fields[0].value, value=msg.embeds[0].fields[1].value, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No clip suggestions found.")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'clip-suggestions' not found!")

bot.run('MTI0MzE5MTExMDQ0NTMwMTc3MA.G-OufL.93LOVnzI_N27_rpU_Xly_cRwQkdU6iYiIIyPjM')
