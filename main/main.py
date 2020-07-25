import discord
from discord.ext import  commands
import json

with open('./resources/help.json', 'r') as fp:
    helpuser = json.load(fp)
    fp.close()

with open('./resources/credential.json', 'r') as fp:
    credentials = json.load(fp)
    fp.close()

token = credentials["token"]

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print("Ad Astra -  ready ")

@client.event
async def on_member_join(member):
    print(f'{member} has joined HorseRadish')
    print("Welcome , いらっしゃい , 어서 오십시오")

@client.event
async  def on_guild_join(guild):
    general = discord.utils.find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}, Ad Astra - At Your Service!'.format(guild.name,))

@client.command()
async def funfact(ctx):
    await ctx.send("Type !octopus")

@client.command()
async def octopus(ctx):
    await ctx.send(helpuser["octopus"])

client.run(token)