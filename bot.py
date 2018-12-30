print("Starting Muffin...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

Client = discord.Client()
bot_prefix= ["m.", "M."]
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='398867510608265221')
footer_text = "═ ∘Our ♡ Server∘ ═"
error_img = ':warning:'
default_invite = 'https://discord.gg/Er3XwBm'
limit = 10000000000000000
version = '1.0'
    
##################################
client.run(os.environ['BOT_TOKEN'])
