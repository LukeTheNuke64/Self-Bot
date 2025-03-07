import discord
from discord.ext import commands

# if you want no prefix leave the string empty
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all(), self_bot=True)


TOKEN = "Discord account token here"
SPAMMED_MESSAGE = "Message here"

@bot.event
async def on_ready():
    print(f"{bot.user.name} connected to discord") # change status and activity below
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=""))

@bot.command() # test if the bot is working
async def ping(ctx):
    await ctx.send("pong")


@bot.command() # sends a message in all channels within every server that the Discord account is in
async def spam(ctx): 
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send(SPAMMED_MESSAGE)
                print(f"Message sent to {channel.name} in {guild.name}")
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass

@bot.command() # funny to spam people
async def spam(ctx, message):
    for _ in range (30):
        await ctx.send(f"{message}")

# REMEMBER TO - pip install discord.py==1.7.3 and use https://www.python.org/downloads/release/python-3110/     
bot.run(TOKEN, bot=False) 
