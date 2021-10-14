import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio
import keep_alive

# For  intents
intents = discord.Intents.all()

# Code for  load settings
with open('setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)


bot = commands.Bot(command_prefix= jdata['Prefix'], 
										 owner_ids= jdata['Owner_id'])

# Event after Bot is online 
@bot.event
async def on_ready():
	print(">> Bot is online <<")

@bot.command()
async def pict(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)

@bot.command()
async def pic(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file= pic )

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} Join !')


# Members Leave
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} Leave !')

# All the cog from cmds
for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])

	
