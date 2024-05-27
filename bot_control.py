from collections import defaultdict, deque
from datetime import datetime, timedelta
from discord.ext import commands, tasks

class BotControl:
    def __init__(self):
        self.bot_active = True
        self.protection_mode = False
        self.message_timestamps = defaultdict(lambda: deque(maxlen=5))
        self.user_messages = defaultdict(list)
        self.join_timestamps = deque(maxlen=10)  # Track recent joins

    def toggle_bot(self):
        self.bot_active = not self.bot_active
        return self.bot_active

    def toggle_protection(self):
        self.protection_mode = not self.protection_mode
        return self.protection_mode

    def activate_protection_for_30_minutes(self):
        self.protection_mode = True
        deactivate_protection_mode.start()

    def check_message(self, member_id, message):
        now = datetime.now()
        timestamps = self.message_timestamps[member_id]
        timestamps.append(now)
        self.user_messages[member_id].append(message)
        if len(timestamps) == 5 and (now - timestamps[0]).seconds < 10:
            return True  # Detected spamming
        return False

    def get_user_messages(self, member_id):
        return self.user_messages[member_id]

    def clear_user_messages(self, member_id):
        self.user_messages[member_id].clear()

    def check_mass_join(self):
        now = datetime.now()
        self.join_timestamps.append(now)
        if len(self.join_timestamps) == 10 and (now - self.join_timestamps[0]).seconds < 60:
            return True  # Detected mass joining
        return False

bot_control = BotControl()

@tasks.loop(minutes=30, count=1)
async def deactivate_protection_mode():
    bot_control.protection_mode = False

def check_bot_active():
    async def predicate(ctx):
        if ctx.author.name == 'sirvosef':
            return True
        if not bot_control.bot_active:
            await ctx.send("The bot is currently off.")
            return False
        return True
    return commands.check(predicate)

def check_protection_mode():
    async def predicate(ctx):
        if not bot_control.protection_mode:
            await ctx.send("Protection mode is currently off.")
            return False
        return True
    return commands.check(predicate)

def rate_limit():
    timestamps = defaultdict(lambda: datetime.min)
    def decorator(func):
        async def wrapper(ctx, *args, **kwargs):
            now = datetime.now()
            if (now - timestamps[ctx.author.id]).seconds < 5:
                await ctx.send("You're sending commands too quickly. Please wait a moment.")
                return
            timestamps[ctx.author.id] = now
            await func(ctx, *args, **kwargs)
        return wrapper
    return decorator
