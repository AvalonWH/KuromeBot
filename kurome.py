import discord
from discord.ext import commands
from dotenv import load_dotenv
from ping import Ping
from help import Help
from join import Join
from leave import Leave
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} Ha despertado ^-^!')
    
    await bot.change_presence(activity=discord.CustomActivity(name="-help"))
    
    await bot.load_extension('ping')
    await bot.load_extension('help')
    await bot.load_extension('join')
    await bot.load_extension("leave")

bot.run(TOKEN)