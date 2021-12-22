from PIL import Image


class Summoner:
    def __init__(self, profile, stats):
        self.name = stats[0]['summonerName']
        self.profile_icon_id = profile['profileIconId']
        self.profile_icon = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{self.profile_icon_id}.png'
        self.level = profile['summonerLevel']
        self.tier = stats[0]['tier']
        self.rank = stats[0]['rank']
        self.lp = stats[0]['leaguePoints']
        self.wins = stats[0]['wins']
        self.losses = stats[0]['losses']
        self.wr = int((self.wins/(self.wins+self.losses)) * 100)
        #self.emblem = self.getEmblem(self.tier)
        #self.opgg_url = f'https://{self.region}.op.gg/summoner/userName={self.name}'

    # def getEmblem(tier):
        # return Image.open(f'./ranked-emblems/{tier}.png')
