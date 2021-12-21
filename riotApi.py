from riotwatcher import LolWatcher, ApiError
import pandas as pd
import utils
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


async def getSummoner(name, region):
    region = region.lower()
    if region not in regions:
        print("Region not found!")
        return "region not found"
    region = regions[region]
    me = watcher.summoner.by_name(region, name)
    return me
