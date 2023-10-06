import discord
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'hemos iniciado sección como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)
    
@bot.command()
async def res(ctx, a: int, b: int):
    await ctx.send(a - b)
    
@bot.command()
async def por(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def div(ctx, a: int, b: int):
    await ctx.send(a / b)
