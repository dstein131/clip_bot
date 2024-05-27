import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
from collections import defaultdict
from datetime import datetime, timedelta

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

bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

# Tracking incorrect command usage
incorrect_command_usage = defaultdict(lambda: {'count': 0, 'last_time': None, 'blocked_until': None})
bot_active = True

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Command to turn the bot on and off
@bot.command(name='toggle_bot')
async def toggle_bot(ctx):
    global bot_active
    if ctx.author.name == 'sirvosef':
        bot_active = not bot_active
        state = "on" if bot_active else "off"
        await ctx.send(f"The bot is now {state}.")
    else:
        await ctx.send("Only Lord Vosef may do this.")

# Fun Feature: Kek
@bot.command(name='kek')
async def kek(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    if ctx.author.name != 'sirvosef':
        await ctx.send("Only Lord Vosef may do this.")
        return

    try:
        print(f'!kek command received in channel: {ctx.channel} by user: {ctx.author}')
        memes = [
            "https://i.imgur.com/tCVnQmi.jpeg",
            "https://i.imgur.com/V08th3K.jpeg",
            "https://i.imgur.com/4iwihon.jpeg",
            "https://www.thepinknews.com/wp-content/uploads/2021/04/Morrissey.jpg"
        ]
        selected_meme = random.choice(memes)
        print(f'Sending meme: {selected_meme}')
        await ctx.send(selected_meme)
    except Exception as e:
        print(f'Error in !kek command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: April
@bot.command(name='April')
async def april(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!April command received in channel: {ctx.channel} by user: {ctx.author}')
        april_images = [
            "https://i.imgur.com/JJVOpgz.png",
            "https://i.imgur.com/r95GXHQ.png",
            "https://i.imgur.com/k6FatNM.png",
            "https://i.imgur.com/BGvYhvE.jpeg",
            "https://i.imgur.com/3xqTqpq.gif",
            "https://i.imgur.com/NE9BsRN.jpeg",
            "https://i.imgur.com/922Bazc.gif",
        ]
        selected_image = random.choice(april_images)
        print(f'Sending April image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !April command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Nic
@bot.command(name='Nic')
async def nic(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!nic command received in channel: {ctx.channel} by user: {ctx.author}')
        nic_images = [
            "https://i.imgur.com/ohG24kL.gif",
            "https://i.imgur.com/fJETMJf.gif",
        ]
        selected_image = random.choice(nic_images)
        print(f'Sending Nic image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !nic command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Lew
@bot.command(name='Lew')
async def lew(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!lew command received in channel: {ctx.channel} by user: {ctx.author}')
        lew_images = [
            "https://i.imgur.com/ucJ1W0y.gif",
            "https://i.imgur.com/cvxUeHO.png",
            "https://i.imgur.com/8QKPnX4.jpeg",
            "https://i.imgur.com/vmt0pqa.jpeg",
            "https://i.imgur.com/TJEyVCr.jpeg",
            "https://i.imgur.com/vKXqnXl.png",
            "https://i.imgur.com/blS4QRI.jpeg",
            "https://i.imgur.com/OvJLNDp.png",
            "https://i.imgur.com/qFvZ7Xp.png",
            "https://i.imgur.com/l417K0B.png",
            "https://i.imgur.com/POpymIg.png",
            "https://i.imgur.com/GqBHXBF.png",
            "https://i.imgur.com/kS94IHL.jpeg",
        ]
        selected_image = random.choice(lew_images)
        print(f'Sending Lew image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !lew command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Vosef
@bot.command(name='Vosef')
async def vosef(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!Vosef command received in channel: {ctx.channel} by user: {ctx.author}')
        vosef_images = [
            "https://i.imgur.com/N5RwnLZ.jpeg"
        ]
        selected_image = random.choice(vosef_images)
        print(f'Sending Vosef image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !Vosef command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: SteelToe
@bot.command(name='SteelToe')
async def steeltoe(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!SteelToe command received in channel: {ctx.channel} by user: {ctx.author}')
        await ctx.send("https://www.youtube.com/watch?v=0WAghhHjGA0&list=PLmXO3OWrzyK2lrh9wsL3ITq9oUcVgoZZS")
    except Exception as e:
        print(f'Error in !SteelToe command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Felicia
@bot.command(name='Felicia')
async def felicia(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!Felicia command received in channel: {ctx.channel} by user: {ctx.author}')
        felicia_images = [
            "https://i.imgur.com/H2l18ml.gif",
            "https://i.imgur.com/PTPhfBq.png"
        ]
        selected_image = random.choice(felicia_images)
        print(f'Sending Felicia image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !Felicia command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: KB
@bot.command(name='KB')
async def kb(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!KB command received in channel: {ctx.channel} by user: {ctx.author}')
        kb_images = [
            "https://imgur.com/yOIsxni",
            "https://i.imgur.com/nXszoyR.png",
            "https://i.imgur.com/QxjvzQx.png",
            "https://i.imgur.com/hknTfbn.jpeg",
        ]
        selected_image = random.choice(kb_images)
        print(f'Sending KB image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !KB command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Moody
@bot.command(name='Moody')
async def moody(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!Moody command received in channel: {ctx.channel} by user: {ctx.author}')
        moody_image = "https://i.imgur.com/NvXIKbQ.jpeg"
        print(f'Sending Moody image: {moody_image}')
        await ctx.send(moody_image)
    except Exception as e:
        print(f'Error in !Moody command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Aaron
@bot.command(name='Aaron')
async def aaron(ctx):
    if not bot_active:
        await ctx.send("The bot is currently off.")
        return

    try:
        print(f'!Aaron command received in channel: {ctx.channel} by user: {ctx.author}')
        aaron_images = [
            "https://i.imgur.com/wicH2Hz.jpeg",
            "https://i.imgur.com/M1umG2R.jpeg",
            "https://i.imgur.com/lzZ5GU5.jpeg",
            "https://i.imgur.com/adQ70ba.jpeg",
            "https://i.imgur.com/YDbHL4Y.jpeg",
            "https://i.imgur.com/rZOxtGZ.jpeg",
            "https://i.imgur.com/LUIBmKi.gif",
            "https://i.imgur.com/jbULtGw.jpeg",
            "https://i.imgur.com/GkTXkhb.jpeg",
            "https://i.imgur.com/4N2SgmF.png",
            "https://i.imgur.com/fvyRGhd.png",
            "https://i.imgur.com/Sni6RYQ.jpeg",
        ]
        selected_image = random.choice(aaron_images)
        print(f'Sending Aaron image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !Aaron command: {e}')
        await ctx.send("An error occurred while processing the command.")

# Command to list all commands
@bot.command(name='List')
async def list_commands(ctx):
    if not bot_active and ctx.author.name != 'sirvosef':
        await ctx.send("The bot is currently off.")
        return

    commands_list = sorted([command.name for command in bot.commands if command.name not in ['kek', 'help']])
    commands_string = "\n".join([f"!{command}" for command in commands_list])
    await ctx.send(f"```Available commands:\n{commands_string}```")

# Respond to specific commands
@bot.event
async def on_message(message):
    if not bot_active and message.author.name != 'sirvosef':
        return

    # Check if the message starts with any of the specified commands
    forbidden_commands = ['!pussy', '!ass', '!tits', '!boobs', '!nudes', '!xxx', '!cock', '!porn', '!nudes', '!dick', '!fuck', '!shit']
    if message.content.lower() in forbidden_commands:
        await message.channel.send('Go Pee Pee, Go Night Night Incel.')
    else:
        # Process commands normally
        await bot.process_commands(message)

    # Additional responses to specific users
    if message.author.name == 'regalsalvatore' and not message.author.bot:
        if random.random() < 0.3:  # 30% chance
            await message.channel.send('jajajajaja')
    if message.author.name == 'natclo5710' and not message.author.bot:
        if random.random() < 0.15:  # 15% chance
            await message.add_reaction('🇬')
            await message.add_reaction('🇦')
            await message.add_reaction('🇾')

# Error Handling
@bot.event
async def on_command_error(ctx, error):
    if not bot_active and ctx.author.name != 'sirvosef':
        await ctx.send("The bot is currently off.")
        return

    user = ctx.author

    if user.name == 'sirvosef':
        await ctx.send("Command not found. Type `!List` to see all available commands.")
        return

    now = datetime.now()
    user_data = incorrect_command_usage[user.id]
    
    # Check if user is blocked
    if user_data['blocked_until'] and now < user_data['blocked_until']:
        await ctx.send("You are temporarily blocked from using commands.")
        return

    # Reset the count if more than 15 seconds have passed since the last incorrect command
    if user_data['last_time'] and (now - user_data['last_time']).seconds > 15:
        user_data['count'] = 0

    user_data['count'] += 1
    user_data['last_time'] = now

    if user_data['count'] >= 2:
        await ctx.send("Don't be a dumb dumb.")
        user_data['blocked_until'] = now + timedelta(minutes=30)
        user_data['count'] = 0
    else:
        await ctx.send("Command not found. Type `!List` to see all available commands.")
    
    print(f'Error: {error}')
    if not isinstance(error, commands.CommandNotFound):
        await ctx.send("An error occurred.")
        raise error

# Run the bot
bot.run(TOKEN)
