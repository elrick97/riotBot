from riotwatcher import LolWatcher, ApiError
import pandas as pd
import utils
#global variables

api_key = utils.get_keys("./.secret/secrets.json", "RIOT_KEY")
watcher = LolWatcher(api_key)
region = 'na1'


async def getSummoner(name, region):
    me = watcher.summoner.by_name(region, name)
    print(me)
