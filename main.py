import discord, asyncio, random
from discord.ext import commands

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all(), self_bot=True)


TOKEN = "MTAwODA5NzgxMjk0NjM2MjQ3OA.GsEdP_.vFZdXpxuZXBcnO8baF9uhVJ1AW8YR5dnAVCOtE"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def hi(ctx, *, message: str="@everyone hi"):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send(message)
                print(f"Message sent to {channel.name} in {guild.name}")
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass

@bot.command()
async def spam(ctx, name):
    for _ in range (30):
        await ctx.send(f"{name}")

        
bot.run(TOKEN, bot=False) 