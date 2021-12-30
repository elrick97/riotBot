import discord
from discord.colour import Color
import riotApi
from discord.ext import commands
import utils

client = commands.Bot(command_prefix='!')

discord_key = utils.get_keys('./.secret/secrets.json', 'BOT_KEY')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('League of Legends'))
    print('bot is ready')


@client.command()
async def whois(ctx, *args):
    tlist = list(args)
    region = tlist[0]
    print(region)
    del tlist[0]
    id = " ".join(tlist)
    print(id)
    print('command whois called')
    res = await riotApi.getSummoner(region, id)
    if(not res.unranked):
        embed = discord.Embed(color=0x71f79f)
        embed.set_author(name=res.name, url=res.opgg_url,
                         icon_url=res.profile_icon)
        embed.title = f'{res.tier.capitalize()} {res.rank}'
        embed.description = f'Level: {res.level} - LP: {res.lp}'
        embed.add_field(name='WR', value=f'{res.wr}%', inline=True)
        embed.add_field(name='Wins', value=res.wins, inline=True)
        embed.add_field(name='Losses', value=res.losses, inline=True)
        embed.add_field(name='Queue', value=res.queue, inline=True)
        embed.set_thumbnail(url=res.emblem)
    else:
        if(not res.error):
            embed = discord.Embed(color=0x71f79f)
            embed.set_author(name=res.name, icon_url=res.profile_icon)
            embed.title = res.tier
            embed.description = f'Level: {res.level}'
            embed.set_thumbnail(
                url='https://lolg-cdn.porofessor.gg/img/s/league-icons-v2/160/0-0.png')
        else:
            embed = discord.Embed(color=0x71f79f)
            embed.set_author(name=res.name)
            embed.title = 'Check spelling'
    await ctx.send(embed=embed)

client.run(discord_key)
