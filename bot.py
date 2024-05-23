import discord
from discord.ext import commands

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
    # Only allow the bot to read from the 'nlo-suggestions' channel
    if ctx.channel.name != 'nlo-suggestions':
        await ctx.send("Please use the `nlo-suggestions` channel for adding suggestions.")
        return

    channel = discord.utils.get(ctx.guild.text_channels, name='private-nlo-suggestions')
    if channel:
        embed = discord.Embed(title="New Suggestion", color=discord.Color.blue())
        embed.add_field(name="URL", value=url, inline=False)
        embed.add_field(name="Timestamp", value=timestamp, inline=True)
        embed.add_field(name="Description", value=description, inline=True)
        embed.set_footer(text=f"Suggested by {ctx.author}")
        await channel.send(embed=embed)
        await ctx.send("Suggestion added!")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'private-nlo-suggestions' not found!")

# Command to list all suggestions
@bot.command(name='listall')
async def list_all(ctx):
    # Only allow the bot to list suggestions in the 'private-nlo-suggestions' channel
    if ctx.channel.name != 'private-nlo-suggestions':
        await ctx.send("Please use the `private-nlo-suggestions` channel for listing suggestions.")
        return

    channel = discord.utils.get(ctx.guild.text_channels, name='private-nlo-suggestions')
    if channel:
        messages = await channel.history(limit=100).flatten()
        if messages:
            embed = discord.Embed(title="Suggestions", color=discord.Color.green())
            for msg in messages:
                if msg.embeds:
                    embed.add_field(name=msg.embeds[0].fields[1].value, value=msg.embeds[0].fields[2].value, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No suggestions found.")
    else:
        print(f"Available channels: {[c.name for c in ctx.guild.text_channels]}")  # Debugging: print available channels
        await ctx.send("Channel 'private-nlo-suggestions' not found!")

bot.run('DISCORD_BOT_TOKEN')
