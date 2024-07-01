import random
import discord
from discord.ext import commands
from bot_control import check_bot_active, rate_limit

# Fun Feature: Kek (Excluded from !list)
@commands.command(name='kek')
@check_bot_active()
@rate_limit()
async def kek(ctx):
    if ctx.author.name != 'sirvosef':
        await ctx.send(":frog:")
        return

    try:
        print(f'!kek command received in channel: {ctx.channel} by user: {ctx.author}')
        memes = [
            "https://i.imgur.com/ezA43qN.gif",
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
            "https://i.imgur.com/mrhXv8M.gif",
            "https://i.imgur.com/JryN4X7.png",
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
            "https://i.imgur.com/yLhEKnF.jpeg",
            "https://i.imgur.com/qNrhstY.png",
            "https://i.imgur.com/BKN3Lep.png",
            "https://i.imgur.com/rSXYoMh.png",
            "https://i.imgur.com/WV0UvWW.png",
            "https://i.imgur.com/Xucq0Pp.gif",
            "https://i.imgur.com/cbCGNvl.png",
            "https://i.imgur.com/1AB8LWM.jpeg",
            "https://i.imgur.com/8X6gQq0.png",
            "https://i.imgur.com/lxUkWeO.gif",
            "https://i.imgur.com/EeWSJUX.jpeg",
            "https://i.imgur.com/QSmV65g.png",
            "https://i.imgur.com/77LpeIj.jpeg",
            "https://i.imgur.com/4UHVvzb.jpeg",
            "https://i.imgur.com/LsxCN1H.gif",
            "https://i.imgur.com/h81woBE.jpeg",
            "https://i.imgur.com/ILGXtuP.gif",
            "https://i.imgur.com/8rqttQB.png",
        ]
        
        lew_videos = [
            "./videos/lewwho.mov",
            "./videos/My_Movie_4.mov",
            # Add more video paths here if needed
        ]
        
        # Combine images and videos into one list
        lew_media = lew_images + lew_videos
        selected_media = random.choice(lew_media)
        
        if selected_media in lew_images:
            print(f'Sending Lew image: {selected_media}')
            await ctx.send(selected_media)
        else:
            print(f'Sending Lew video: {selected_media}')
            await ctx.send(file=discord.File(selected_media))
            
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
            "https://i.imgur.com/PTPhfBq.png",
            "https://i.imgur.com/0OW42ZM.png",
            "https://i.imgur.com/LMtMdqp.jpeg",
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
            "https://i.imgur.com/ZMA00HT.gif",
        ]

        kb_videos = [
            "./videos/kbcough.mov",
            "./videos/kbcummy.mov",
            # Add more video file paths or URLs here
        ]

        # Combine images and videos into one list
        kb_media = kb_images + kb_videos
        selected_media = random.choice(kb_media)

        if selected_media in kb_images:
            print(f'Sending KB image: {selected_media}')
            await ctx.send(selected_media)
        else:
            print(f'Sending KB video: {selected_media}')
            await ctx.send(file=discord.File(selected_media))
        
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
        moody_images = [
            "https://i.imgur.com/NvXIKbQ.jpeg",
            "https://i.imgur.com/THWvdum.gif",
            "https://i.imgur.com/KFHsEdi.gif",
            "https://i.imgur.com/CcSrI8a.png",
            "https://i.imgur.com/mpBqBks.png",
            "https://i.imgur.com/YFfDgx8.png",
            "https://i.imgur.com/HwRTje9.gif",
        
    
        ]
        selected_image = random.choice(moody_images)
        print(f'Sending Moody image: {selected_image}')
        await ctx.send(selected_image)
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
            "https://i.imgur.com/L5JAwvT.gif",
            "https://i.imgur.com/wV0vLcr.png",
            "https://i.imgur.com/mZJGapd.jpeg",
            "https://i.imgur.com/VGGl17W.gif",
            "https://i.imgur.com/4oarokq.png",
            "https://i.imgur.com/a5zZvbp.png",
            "https://i.imgur.com/PdMKavl.png",
            "https://i.imgur.com/pIB8xK0.gif",
            "https://i.imgur.com/pMrD82Z.png",
            "https://i.imgur.com/nEDfBHX.png",
            "https://i.imgur.com/JP6KSx6.gif",
            "https://i.imgur.com/RI3pvc0.gif",
            "https://i.imgur.com/Qxp7sok.gif",
            "https://i.imgur.com/eGwbgpk.jpeg",
            "https://i.imgur.com/xonER0x.png",

           
        ]
        selected_image = random.choice(aaron_images)
        print(f'Sending Aaron image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !Aaron command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: MKE
@commands.command(name='mke')
@check_bot_active()
@rate_limit()
async def mke(ctx):
    try:
        print(f'!MKE command received in channel: {ctx.channel} by user: {ctx.author}')
        mke_images = [
            "https://i.imgur.com/NtWJCqc.png",
            "https://i.imgur.com/r8jyRMh.png",
            "https://i.imgur.com/7GvXLuC.png",
        ]

        mke_videos = [
            # "./videos/TND_MKE.mov",
        ]
        
        # Combine images and videos into one list
        mke_media = mke_images + mke_videos
        selected_media = random.choice(mke_media)
        
        if selected_media in mke_images:
            print(f'Sending MKE image: {selected_media}')
            await ctx.send(selected_media)
        else:
            print(f'Sending MKE video: {selected_media}')
            await ctx.send(file=discord.File(selected_media))
        
    except Exception as e:
        print(f'Error in !MKE command: {e}')
        await ctx.send("An error occurred while processing the command.")

# New Feature: ray
@commands.command(name='ray')
@check_bot_active()
@rate_limit()
async def ray(ctx):
    try:
        print(f'!ray command received in channel: {ctx.channel} by user: {ctx.author}')
        ray_images = [
            "https://i.imgur.com/Vf7tcWk.png",
            "https://i.imgur.com/Vr1s4is.png",
            "https://i.imgur.com/JQpYwMH.png",
            "https://i.imgur.com/DEwiNtJ.png",
            "https://i.imgur.com/BZOAHna.png",


        ]
        selected_image = random.choice(ray_images)
        print(f'Sending ray image: {selected_image}')
        await ctx.send(selected_image)
    except Exception as e:
        print(f'Error in !ray command: {e}')
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
    bot.add_command(mke)
    bot.add_command(ray)
