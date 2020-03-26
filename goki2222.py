import discord
import subprocess
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='%')
loopEvent = asyncio.Event()
loopReady = asyncio.Event()


#on connection print name in console
@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))
	print(bot.user.name)

#VoiceChannel object, use connect()
@bot.command(pass_context=True)
async def join(ctx):
	print("Joining:" + str(ctx.message.author.voice.channel))
	await ctx.channel.send("Joining: " + str(ctx.message.author.voice.channel))
	channel = ctx.message.author.voice.channel
	await channel.connect()
	
#voiceClient object, use disconnect()
@bot.command(pass_context=True)
async def leave(ctx):
	print("Leaving:" + str(ctx.message.author.voice.channel))
	await ctx.channel.send("Leaving: " + str(ctx.message.author.voice.channel))
	server = ctx.message.guild.voice_client
	await server.disconnect()
	

@bot.command(pass_context=True)
async def cowards(ctx):
	await ctx.channel.send("Now Playing: \"You'll Cowards Don't Even Smoke Crack\"" + str(ctx.message.author.voice.channel))
	server = ctx.message.guild.voice_client
	server.play(discord.FFmpegPCMAudio("cowards.mp3"))

@bot.command(pass_context=True)
async def testYtdl(ctx):
	await ctx.channel.send("Downloading..." + str(ctx.message.author.voice.channel))
	subprocess.call("./dl https://www.youtube.com/watch?v=0gi-RYNhP8Y -x --audio-format mp3 --output \"audio.%(ext)s\"", shell=True)
	server = ctx.message.guild.voice_client
	server.play(discord.FFmpegPCMAudio("audio.mp3"))

@bot.command(pass_context=True)
async def halp(ctx):
	await ctx.channel.send("""goki.py Commands:\n
	%join: gokiburi joins voice channel\n
	%leave: gokiburi leaves voicechannel\n
	%cowards: viper plays if gokiburi is in vc\n
	%testYtdl: gokiburi will download cancer and play it for vc\n
	%help: helps you""")
	

@bot.command(pass_context=True)
async def immm(ctx):
	server = ctx.message.guild.voice_client
	server.play(discord.FFmpegPCMAudio("output.mp3"))

	while 1:
		await asyncio.sleep(1)
		if server.is_playing() == False:
			break
	print("DONE")
	await immm(ctx)
	
	
client.loop.create_task(ironmanCheckAudio())
bot.run('FNFADJAKJLASDJK MY KEY AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
