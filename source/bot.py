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

@bot.command( name = 'zoltar', help = 'Ask Zoltar a question about the future and be enlightened' )
async def zoltar( ctx ) :
    answers = [
        "It is certain",
        "My reply is no",
        "You may rely on it",
        "Outlook good",
        "You shall not know the answer before it happens",
        "I would say... yes!",
        "The answers you seek are where you least want to look.",
        "It is possible, although not very likely.",
        "I can only advise that you do not make any assumptions.",
        "Better luck next time kid",
        "The world seems to be on your shoulders. Smile, and let it go",
        "I was told it is unlikely",
        "Only you can control your destiny.",
        "Absolutely not",
        "The spirit world has not decided.",
        "Does the pope shit in the woods?",
        "Yes! that is almost as certain as rob ending up in the drunk tank.",
        "Does Abel keep a thick bitch?",
        "You will almost certainly be disappointed in the outcome.",
        "A resounding yes",
        "You are looking in the wrong place.",
        "Perhaps in another life."
    ]

    response = random.choice( answers )
    await ctx.send( response )

bot.run(TOKEN)
