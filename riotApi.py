from riotwatcher import LolWatcher, ApiError
from Summoner import Summoner
import utils
import discord
#global variables

api_key = utils.get_keys("./.secret/secrets.json", "RIOT_KEY")
watcher = LolWatcher(api_key)
region = 'na1'
regions = {"na": "na1",
           "lan": "la1",
           "euw": "euw1",
           "eun": "eun1",
           "br": "br1",
           "jp": "jp1",
           "kr": "kr1",
           "oc": "oc1",
           "tr": "tr1",
           "ru": "ru1"}


async def getSummoner(region, name):
    nregion = region
    region = region.lower()
    if region not in regions:
        print("Region not found!")
        return Summoner({}, {}, 'Region not found')
    region = regions[region]
    try:
        me = watcher.summoner.by_name(region, name)
        my_ranked_stats = watcher.league.by_summoner(region, me['id'])
        return Summoner(me, my_ranked_stats, nregion)
    except:
        print("summoner not found")
        return Summoner({}, {}, 'Summoner not found')


def buildMessage(profile, stats):
    name = stats[0]['summonerName']
    profile_icon_id = profile['profileIconId']
    profile_icon = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{profile_icon_id}.png'
    level = profile['summonerLevel']
    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']
    wins = stats[0]['wins']
    losses = stats[0]['losses']
    wr = int((wins/(wins+losses)) * 100)
    opgg_url = f'https://{region}.op.gg/summoner/userName={name}'
    print(name, profile_icon, level, tier,
          rank, lp, wins, losses, wr, opgg_url)
