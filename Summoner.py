QUEUES = {
    'RANKED_FLEX_SR': 'Flexq',
    'RANKED_SOLO_5x5': 'Soloq'
}


class Summoner:

    def __init__(self, profile, stats, nregion):
        if(not bool(profile)):
            print("summoner not found")
            self.unranked = True
            self.error = True
            self.name = nregion
            return
        print(profile, stats)
        self.stats = stats
        queue = self.getQueue()
        if(queue != "weird" and bool(stats)):
            self.unranked = False
            self.queue = QUEUES[queue['queueType']]
            self.name = queue['summonerName']
            self.profile_icon_id = profile['profileIconId']
            self.profile_icon = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{self.profile_icon_id}.png'
            self.level = profile['summonerLevel']
            self.tier = queue['tier']
            self.rank = queue['rank']
            self.lp = queue['leaguePoints']
            self.wins = queue['wins']
            self.losses = queue['losses']
            self.wr = int((self.wins/(self.wins+self.losses)) * 100)
            self.emblem = f'https://lolg-cdn.porofessor.gg/img/s/league-icons-v2/160/{self.getEmblemId()}-1.png'
            self.opgg_url = f'https://{nregion}.op.gg/summoner/userName={self.name}'.replace(
                " ", "%20")
        else:
            self.unranked = True
            self.error = False
            print(queue)
            self.name = profile['name']
            self.profile_icon_id = profile['profileIconId']
            self.profile_icon = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{self.profile_icon_id}.png'
            self.level = profile['summonerLevel']
            self.tier = 'Unranked'

    def getQueue(self):
        for queue in self.stats:
            print(queue)
            if(queue['queueType'] == 'RANKED_FLEX_SR' or queue['queueType'] == 'RANKED_SOLO_5x5'):
                return queue
            else:
                return "weird"

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
