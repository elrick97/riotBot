import discord
import riotApi
from discord.ext import commands
import utils

client = commands.Bot(command_prefix='/')

discord_key = utils.get_keys('./.secret/secrets.json', 'BOT_KEY')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('League of Legends'))
    print('bot is ready')


@client.command()
async def whois(ctx, id, region):
    await riotApi.getSummoner(region, id)
    print('command whois called')


client.run(discord_key)
