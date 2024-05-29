import random
from discord.ext import commands
from bot_control import check_bot_active, rate_limit

# Fun Feature: Kek (Excluded from !list)
@commands.command(name='kek')
@check_bot_active()
@rate_limit()
async def kek(ctx):
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
@commands.command(name='april')
@check_bot_active()
@rate_limit()
async def april(ctx):
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
            "https://i.imgur.com/sj2u9H9.png",
            "https://i.imgur.com/r3YcsvQ.jpeg",
            "https://i.imgur.com/KKrxCoZ.png",
        ]
        selected_image = random.choice(april_images)
        print(f'Sending April image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !April command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Nic
@commands.command(name='nic')
@check_bot_active()
@rate_limit()
async def nic(ctx):
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
@commands.command(name='lew')
@check_bot_active()
@rate_limit()
async def lew(ctx):
    try:
        print(f'!lew command received in channel: {ctx.channel} by user: {ctx.author}')
        lew_images = [
            "https://i.imgur.com/ucJ1W0y.gif",
            "https://i.imgur.com/cvxUeHO.png",
            "https://i.imgur.com/8QKPnX4.jpeg",
            "https://i.imgur.com/TJEyVCr.jpeg",
            "https://i.imgur.com/vKXqnXl.png",
            "https://i.imgur.com/blS4QRI.jpeg",
            "https://i.imgur.com/OvJLNDp.png",
            "https://i.imgur.com/qFvZ7Xp.png",
            "https://i.imgur.com/l417K0B.png",
            "https://i.imgur.com/POpymIg.png",
            "https://i.imgur.com/GqBHXBF.png",
            "https://i.imgur.com/kS94IHL.jpeg",
            "https://i.imgur.com/gSPtcgi.png",
            "https://i.imgur.com/dvdQxo8.png",
            "https://i.imgur.com/njKACDR.png",
            "https://i.imgur.com/KhV1eGl.png",
            "https://i.imgur.com/ca9FvkV.gif",
            "https://i.imgur.com/WbK0Uf0.png",
            "https://i.imgur.com/sCuFLi6.png",
            "https://i.imgur.com/vtzZgJs.jpeg",
            "https://i.imgur.com/TJDUGTX.jpeg",
        ]
        selected_image = random.choice(lew_images)
        print(f'Sending Lew image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !lew command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Vosef
@commands.command(name='vosef')
@check_bot_active()
@rate_limit()
async def vosef(ctx):
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
@commands.command(name='steeltoe')
@check_bot_active()
@rate_limit()
async def steeltoe(ctx):
    try:
        print(f'!SteelToe command received in channel: {ctx.channel} by user: {ctx.author}')
        await ctx.send("https://www.youtube.com/watch?v=0WAghhHjGA0&list=PLmXO3OWrzyK2lrh9wsL3ITq9oUcVgoZZS")
    except Exception as e:
        print(f'Error in !SteelToe command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Felicia
@commands.command(name='felicia')
@check_bot_active()
@rate_limit()
async def felicia(ctx):
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
@commands.command(name='kb')
@check_bot_active()
@rate_limit()
async def kb(ctx):
    try:
        print(f'!KB command received in channel: {ctx.channel} by user: {ctx.author}')
        kb_images = [
            "https://imgur.com/yOIsxni",
            "https://i.imgur.com/nXszoyR.png",
            "https://i.imgur.com/QxjvzQx.png",
            "https://i.imgur.com/hknTfbn.jpeg",
            "https://i.imgur.com/JmU55LM.png",
            "https://i.imgur.com/mE6wLqV.jpeg",
        ]
        selected_image = random.choice(kb_images)
        print(f'Sending KB image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !KB command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Moody
@commands.command(name='moody')
@check_bot_active()
@rate_limit()
async def moody(ctx):
    try:
        print(f'!Moody command received in channel: {ctx.channel} by user: {ctx.author}')
        moody_image = "https://i.imgur.com/NvXIKbQ.jpeg"
        print(f'Sending Moody image: {moody_image}')
        await ctx.send(moody_image)
    except Exception as e:
        print(f'Error in !Moody command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: Aaron
@commands.command(name='aaron')
@check_bot_active()
@rate_limit()
async def aaron(ctx):
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
            "https://i.imgur.com/zDLjwmU.png",
            "https://i.imgur.com/VhrI4ub.png",
            "https://i.imgur.com/BKN3Lep.png",
            "https://i.imgur.com/L5JAwvT.gif",
            "https://i.imgur.com/wV0vLcr.png",
           
        ]
        selected_image = random.choice(aaron_images)
        print(f'Sending Aaron image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !Aaron command: {e}')
        await ctx.send("An error occurred while processing the command.")

def setup(bot):
    bot.add_command(kek)
    bot.add_command(april)
    bot.add_command(nic)
    bot.add_command(lew)
    bot.add_command(vosef)
    bot.add_command(steeltoe)
    bot.add_command(felicia)
    bot.add_command(kb)
    bot.add_command(moody)
    bot.add_command(aaron)
