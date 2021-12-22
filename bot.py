import discord
from discord.colour import Color
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
async def whois(ctx, region, id):
    print('command whois called')
    res = await riotApi.getSummoner(region, id)
    embed = discord.Embed(color=0x71f79f)
    embed.set_author(name=res.name, url=res.opgg_url,
                     icon_url=res.profile_icon)
    embed.title = f'{res.tier.capitalize()} {res.rank}'
    embed.description = f'Level: {res.level} - LP: {res.lp}'
    embed.add_field(name='WR', value=f'{res.wr}%', inline=True)
    embed.add_field(name='Wins', value=res.wins, inline=True)
    embed.add_field(name='Losses', value=res.losses, inline=True)
    embed.set_thumbnail(url=res.emblem)
    await ctx.send(embed=embed)


client.run(discord_key)
