
class Summoner:
    regions = {
        ""
    }

    def __init__(self, profile, stats, nregion):
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
        self.emblem = f'https://lolg-cdn.porofessor.gg/img/s/league-icons-v2/160/{self.getEmblemId()}-1.png'
        self.opgg_url = f'https://{nregion}.op.gg/summoner/userName={self.name}'.replace(
            " ", "%20")

    def getEmblemId(self) -> str:
        if(self.tier == 'IRON'):
            return 1
        elif(self.tier == 'BRONZE'):
            return 2
        elif(self.tier == 'SILVER'):
            return 3
        elif(self.tier == 'GOLD'):
            return 4
        elif(self.tier == 'PLATINUM'):
            return 5
        elif(self.tier == 'DIAMOND'):
            return 6
        elif(self.tier == 'MASTER'):
            return 7
        elif(self.tier == 'GRANDMASTER'):
            return 8
        elif(self.tier == 'CHALLENGER'):
            return 9
