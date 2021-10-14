import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
import os, random

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Main(Cog_Extension):

	'''
	For ctx (U can copy and paste this)
	async def user_respone():
		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel
		respone = await self.bot.wait_for('message', check=check)
		return respone

	respone_msg = await user_respone
	'''

	@commands.command()
	async def ping(self, ctx):
		'''Bot Ping'''
		await ctx.send(f'{round(self.bot.latency*1000)} ms')


	@commands.command()
	@check.valid_user() #Check if the user is a valid user
	async def test(self, ctx):
		'''Admin User check'''
		await ctx.send('Bee! Bo!')
		

	@commands.command()
	async def sayd(self, ctx, *, content: str):
		'''Send message'''
		if "@everyone" in content:
			await ctx.send(f"{ctx.author.mention} I love u all")
			return
		else: await ctx.message.delete()
		await ctx.send(content)


	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="About a bot created by Lx", description="Lx BigBrain", color=0x28ddb0)
		# embed.set_thumbnail(url="#")
		embed.add_field(name="Developers", value="Lx (<@!852547642428489738>)", inline=True)
		embed.add_field(name="Version", value="0.1.0 a", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
		embed.set_footer(text="Made with ❤")
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Main(bot))
