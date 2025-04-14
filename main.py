# requirements : pip install discord | pip install mtasanpystatus 
# ------------------------------------------------------------------
# Join discord : https://discord.gg/tEYgv9Gnbd

# Youtube Video : https://youtu.be/srVCmOe0c6E

import discord
from discord.ext import commands
import mtasanpystatus # https://pypi.org/project/mtasanpystatus/

PREFIX="?" # set the prefix you want

intents = discord.Intents.default() # or you can use Intents.all()
intents.message_content = True # if you use discord.Intents.all() delete this line

bot = commands.Bot(command_prefix=PREFIX, intents=intents) # , help_command=None, case_sensitive=False those are not neccesary 

@bot.event
async def on_ready():
    print("bot is online ")

@bot.command(aliases=["ip", "port", "server", "link", "play", "join", "rp"]) # you can use aliases if you want (optional)
async def status(ctx):

    server_address = "your server address"
    ip = "" # set your server ip
    port = 22003 # server port 

    mtasanpystatus.connect(ip, port, timeout=50)


    onlineplayers = mtasanpystatus.players or "0 Playing Now"
    maxplayers = mtasanpystatus.maxplayers or "2048" # or what's your server max players count / value
    servername = mtasanpystatus.name or "Your server name"
    style = mtasanpystatus.gamemode or "Role Play"
    version = mtasanpystatus.version or "1.6"
    city = mtasanpystatus.map or "Los Santos"
    playnow = mtasanpystatus.join_link or server_address #or "discord link"

    # you can use custom emojis if you want 
    embed = discord.Embed(title=servername)

    # -------------------- Old Style -------------------------
    embed.add_field(name="Players :busts_in_silhouette: :", value=f"{onlineplayers}/{maxplayers}", inline=True)
    embed.add_field(name="Game Mode :sparkles: :", value=style, inline= True)
    embed.add_field(name="Server Version :gear: :", value=version, inline=True)
    embed.add_field(name="Map/Location :cityscape: :", value=city , inline= True)
    embed.add_field(name="Join Us :globe_with_meridians: :", value=f"```{playnow}```", inline=False)

    # # -------------------- New style -------------------------
    # embed.add_field(name="Map/Location :cityscape: :", value=f"```{city}```" , inline= True)
    # embed.add_field(name="Server Version :gear: :", value=f"```{version}```", inline=True)
    # embed.add_field(name="", value="", inline=False)
    # embed.add_field(name="Game Mode :sparkles: :", value=f"```{style}```", inline=True)
    # embed.add_field(name="Players :busts_in_silhouette: :", value=f"```{onlineplayers}/{maxplayers}```", inline=True)
    # embed.add_field(name="Join Us :globe_with_meridians: :", value=f"```{playnow}```", inline=False)


    await ctx.send(embed=embed)

BOT_TOKEN= "YOUR BOT TOKEN"

bot.run(BOT_TOKEN)