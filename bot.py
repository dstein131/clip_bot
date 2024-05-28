import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
from collections import defaultdict
from datetime import datetime, timedelta
from bot_control import BotControl, check_bot_active, rate_limit  # Import from the new module
import fun_commands  # Import the fun commands

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
bot_control = BotControl()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    fun_commands.setup(bot)  # Setup fun commands

# Command to turn the bot on and off
@bot.command(name='toggle_bot')
async def toggle_bot(ctx):
    if ctx.author.name == 'sirvosef':
        state = "on" if bot_control.toggle_bot() else "off"
        await ctx.send(f"The bot is now {state}.")
    else:
        await ctx.send("Only Lord Vosef may do this.")

# Command to turn the protection mode on and off
@bot.command(name='toggle_protection')
async def toggle_protection(ctx):
    if ctx.author.name == 'sirvosef':
        state = "on" if bot_control.toggle_protection() else "off"
        await ctx.send(f"Protection mode is now {state}.")
    else:
        await ctx.send("Only Lord Vosef may do this.")

# Command to activate protection mode for 30 minutes
@bot.command(name='activate_protection_30')
async def activate_protection_30(ctx):
    if ctx.author.name == 'sirvosef':
        bot_control.activate_protection_for_30_minutes()
        await ctx.send("Protection mode is now on for 30 minutes.")
    else:
        await ctx.send("Only Lord Vosef may do this.")

# Command to list all commands
@bot.command(name='list')
@check_bot_active()
@rate_limit()
async def list_commands(ctx):
    excluded_commands = ['toggle_bot', 'toggle_protection', 'activate_protection_30', 'kek']
    commands_list = sorted([command.name for command in bot.commands if command.name not in excluded_commands])
    commands_string = "\n".join([f"!{command}" for command in commands_list])
    await ctx.send(f"```Available commands:\n{commands_string}```")

@bot.event
async def on_member_join(member):
    if bot_control.check_mass_join():
        bot_control.activate_protection_for_30_minutes()
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send("Mass joining detected! Protection mode activated for 30 minutes.")

@bot.event
async def on_message(message):
    if not bot_control.bot_active and message.author.name != 'sirvosef':
        return

    if bot_control.protection_mode and bot_control.check_message(message.author.id, message):
        await message.channel.send("You are sending messages too quickly. Please slow down.")
        
        user_messages = bot_control.get_user_messages(message.author.id)
        for msg in user_messages:
            try:
                await msg.delete()
            except discord.NotFound:
                continue
        
        bot_control.clear_user_messages(message.author.id)
        
        join_time = message.author.joined_at
        if (datetime.now() - join_time).days < 1:  # User joined within the last day
            await message.author.kick(reason="Spamming messages")
        else:
            timeout_duration = timedelta(minutes=5)
            until = datetime.now() + timeout_duration
            await message.author.timeout(until=until, reason="Spamming messages")
        return

    await bot.process_commands(message)

    # Additional responses to specific users
    if message.author.name == 'regalsalvatore' and not message.author.bot:
        if random.random() < 0.3:  # 30% chance
            responses = ['jajajajaja', 'jojojojojo', 'jijijijiji', '哈哈哈哈哈哈', '嘻嘻嘻嘻嘻嘻', 'xīxīxīxīxī', 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋ', 'ㅎㅎㅎㅎㅎㅎㅎㅎㅎ', 'jejejejeje']
            selected_response = random.choice(responses)
            await message.channel.send(selected_response)
    if message.author.name == 'natclo5710' and not message.author.bot:
        if random.random() < 0.25:  # 25% chance
            await message.add_reaction('🇬')
            await message.add_reaction('🇦')
            await message.add_reaction('🇾')

@bot.event
async def on_command_error(ctx, error):
    if not bot_control.bot_active and ctx.author.name != 'sirvosef':
        await ctx.send("The bot is currently off.")
        return

    user = ctx.author

    if user.name == 'sirvosef':
        await ctx.send("Command not found. Type `!list` to see all available commands.")
        return

    now = datetime.now()
    user_data = incorrect_command_usage[user.id]
    
    if user_data['blocked_until'] and now < user_data['blocked_until']:
        await ctx.send("You are temporarily blocked from using commands.")
        return

    if user_data['last_time'] and (now - user_data['last_time']).seconds > 15:
        user_data['count'] = 0

    user_data['count'] += 1
    user_data['last_time'] = now

    if user_data['count'] >= 2:
        await ctx.send("Don't be a dumb dumb.")
        user_data['blocked_until'] = now + timedelta(minutes=30)
        user_data['count'] = 0
    else:
        await ctx.send("Command not found. Type `!list` to see all available commands.")
    
    print(f'Error: {error}')
    if not isinstance(error, commands.CommandNotFound):
        await ctx.send("An error occurred.")
        raise error

bot.run(TOKEN)
