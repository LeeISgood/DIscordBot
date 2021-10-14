import discord
from discord.ext import commands
from core.classes import Cog_Extension, Logger
from cmds.main import Main #導入 Main Cog
import json, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Errors():
	"""For error"""

	# 自訂 Error Handler
	@Main.sayd.error
	async def sayd_error(self, ctx, error):
		'''Main.sayd Wrong commands'''
		if isinstance(error, commands.MissingRequiredArgument):
			err = str(error).split(" ")[0]
			await ctx.send(f"Missing： <`{err}`>")
			await ctx.send_help(ctx.command)
			Logger.log(self, ctx, error)
			
	
	# 預設 Error Handler
	async def default_error(self, ctx, error):
		'''default error'''
		
		# 比對觸發的error是否為 MissingRequiredArgument 的實例
		if isinstance(error, commands.MissingRequiredArgument):
			err = str(error).split(" ")[0]
			await ctx.send(f"Missing： <`{err}`>")
			await ctx.send_help(ctx.command)
			Logger.log(self, ctx, error)
		
		# error for 403 Forbiddden
		elif "403 Forbidden" in str(error): 
			await ctx.send("403 Forbidden，Pls check bot permmison")
			Logger.log(self, ctx, error)
		
		# Not
		else:
			await ctx.send(f'unknow error: {error}')
			Logger.log(self, ctx, error)
