import json
import discord
import os
import random
import subprocess

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to discord')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji. ',
        'Bingpot',
        (
            'Cool. Cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='btc', help='Responds with the current price of Bitcoin.')
async def btc(ctx):
    x = subprocess.run(['cryptoco-py', 'sprice', 'bitcoin'], capture_output=True)
    x.check_returncode()
    y = json.loads(x.stdout)

    z = y["bitcoin"]

    zz = z['usd']
    response = "Current price: {}".format(zz)

    await ctx.send(f"Current price: ${zz}")


bot.run(TOKEN)
