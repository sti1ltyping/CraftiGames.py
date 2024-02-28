import aiohttp
import json


class Pikanetwork():
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~


    A basic wrapper for the PikaNetwork's API.
    """
    class __Client_Guild_Profile__:
        def __init__(self, data):
            self.data = data

        async def name(self):
            """Returns guild name.\n~~~"""
            return self.data.get("name", None)
        
        async def tag(self):
            """Returns guild tag.\n~~~"""
            return self.data.get("tag", None)
        
        async def leader(self):
            """Returns username of the guild leader.\n~~~"""
            return self.data.get("owner", {}).get("username", None)
        
        async def level(self):
            """Returns current level of the guild.\n~~~"""
            return self.data.get("leveling",{}).get("level", None)
        
        async def member_list(self):
            """Returns guild members [LIST].\n~~~"""
            members = self.data.get("members", [])
            list = []
            for member in members:
                member_stats = member["user"]["username"]
                list.append(member_stats)
            return list 
        
        async def member_count(self):
            """Returns member count of the guild.\n~~~"""
            members = self.data.get("members", [])
            list = []
            for member in members:
                member_stats = member["user"]["username"]
                list.append(member_stats)
            return int(len(list))
        
        
    class ProfileContext:
        def __init__(self, data):
            self.data = data

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

        async def username(self):
            """Returns username of the player.\n~~~"""
            return self.data.get("username")
        
        async def level(self):
            """Returns current level of the player.\n~~~"""
            return self.data.get("rank", {}).get("level")
        
        async def highest_minigame_rank(self):
            """Returns highest minigame rank of the player.\n~~~"""
            sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
                "developer": 0, "admin": 1,"manager": 2, "srmod": 3, "moderator": 4, "helper": 5, "trial": 6, "youtuber": 7, "champion": 8, "titan": 9, "elite": 10, "vip": 11
            }.get(x.get('displayName', '').lower(), float('inf')))
            return sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'

        
        async def guild(self):
            """Fetch guild of the player.\n~~~\n\nreturn None if guild is not found:\n~~~"""
            if "clan" in self.data and self.data["clan"] is None:
                return None
            
            guild_data = self.data.get("clan", {})
            return Pikanetwork().__Client_Guild_Profile__(guild_data)
        

    class _PlayerStats__BEDWARS_:
        def __init__(self, data):
            self.data = data

        async def wins(self):
            """Returns 'win' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.wins()\n        print('wins:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            wins = self.data.get("Wins", {}).get("entries", [{}])
            value = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard = wins[0].get("place", "0") if wins and wins[0] else "0"
            return value, leaderboard

        async def losses(self):
            """Returns 'losses' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.losses()\n        print('losses:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            return value, leaderboard
        
        async def wlr(self):
            """Returns 'wlr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        wlr = await client.wlr()\n        print('wlr:', wlr)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            wins, _ = await self.wins()
            losse, _ = await self.losses()
            if losse == "0":
                return int(wins)
            else:
                return int(int(wins) / int(losse))

        async def kills(self):
            """Returns 'kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kills()\n        print('kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            kills = self.data.get("Kills", {}).get("entries", [{}])
            value = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard = kills[0].get("place", "0") if kills and kills[0] else "0"
            return value, leaderboard

        async def deaths(self):
            """Returns 'death' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.deaths()\n        print('deaths:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            deaths = self.data.get("Deaths", {}).get("entries", [{}])
            value = deaths[0].get("value", "0") if deaths and deaths[0] else "0"
            leaderboard = deaths[0].get("place", "0") if deaths and deaths[0] else "0"
            return value, leaderboard

        async def kdr(self):
            """Returns 'kdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            kills, _ = await self.kills()
            deaths, _ = await self.deaths()
            if deaths == "0":
                return int(kills)
            else:
                return int(int(kills) / int(deaths))
            
        async def final_kills(self):
            """Returns 'final kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.final_kills()\n        print('final kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Finals_deaths = self.data.get("Final kills", {}).get("entries", [{}])
            value = Finals_deaths[0].get("value", "0") if Finals_deaths and Finals_deaths[0] else "0"
            leaderboard = Finals_deaths[0].get("place", "0") if Finals_deaths and Finals_deaths[0] else "0"
            return value, leaderboard
        
        async def final_deaths(self):
            """Returns 'final deaths' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.final_deaths()\n        print('final deaths:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Finals = self.data.get("Final deaths", {}).get("entries", [{}])
            value = Finals[0].get("value", "0") if Finals and Finals[0] else "0"
            leaderboard = Finals[0].get("place", "0") if Finals and Finals[0] else "0"
            return value, leaderboard
        
        async def fkdr(self):
            """Returns 'fkdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        fkdr = await client.fkdr()\n        print('fkdr:', fkdr)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            final_kills, _ = await self.final_kills()
            final_deaths, _ = await self.final_deaths()
            if final_deaths == "0":
                return int(final_kills)
            else:
                return int(int(final_kills) / int(final_deaths))
            
        async def bed_destroyed(self):
            """Returns 'bed destroyed' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.bed_destroyed()\n        print('bed destroyed:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            beds_destroyed = self.data.get("Beds destroyed", {}).get("entries", [{}])
            value = beds_destroyed[0].get("value", "0") if beds_destroyed and beds_destroyed[0] else "0"
            leaderboard = beds_destroyed[0].get("place", "0") if beds_destroyed and beds_destroyed[0] else "0"
            return value, leaderboard
        
        async def highest_win_streak_reached(self):
            """Returns 'highest win streak reached' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.highest_win_streak_reached()\n        print('highest winstreak reached:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Winstreak = self.data.get("Highest winstreak reached",{}).get("entries", [{}])
            value = Winstreak[0].get("value", "0") if Winstreak and Winstreak[0] else "0"
            leaderboard = Winstreak[0].get("place", "0") if Winstreak and Winstreak[0] else "0"
            return value, leaderboard
        
        async def bow_kills(self):
            """Returns 'bow kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.bow_kills()\n        print('bow kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Bow_kills = self.data.get("Bow_kills", {}).get("entries", [{}])
            value = Bow_kills[0].get("value", "0") if Bow_kills and Bow_kills[0] else "0"
            leaderboard = Bow_kills[0].get("place", "0") if Bow_kills and Bow_kills[0] else "0"
            return value, leaderboard
        
        async def games_played(self):
            """Returns 'games played' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.games_played()\n        print('total number of games played:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            return value, leaderboard
        
        async def arrow_hit(self):
            """Returns 'arrow hit' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.arrow_hit()\n        print('arrow hit:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            arrows_hit = self.data.get("Arrows hit", {}).get("entries", [{}])
            value = arrows_hit[0].get("value", "0") if arrows_hit and arrows_hit[0] else "0"
            leaderboard = arrows_hit[0].get("place", "0") if arrows_hit and arrows_hit[0] else "0"
            return value, leaderboard
        
        async def melee_kills(self):
            """Returns 'melee kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.melee_kills()\n        print('melee kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            melee_kills = self.data.get("Melee kills", {}).get("entries", [{}])
            value = melee_kills[0].get("value", "0") if melee_kills and melee_kills[0] else "0"
            leaderboard = melee_kills[0].get("place", "0") if melee_kills and melee_kills[0] else "0"
            return value, leaderboard
        
        async def void_kills(self):
            """Returns 'void kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.void_kills()\n        print('void kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            void_kills = self.data.get("Void kills", {}).get("entries", [{}])
            value = void_kills[0].get("value", "0") if void_kills and void_kills[0] else "0"
            leaderboard = void_kills[0].get("place", "0") if void_kills and void_kills[0] else "0"
            return value, leaderboard
        

    class _PlayerStats__SKYWARS_:
        def __init__(self, data):
            self.data = data

        async def wins(self):
            """Returns 'wins' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.wins()\n        print('games won:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            wins = self.data.get("Wins", {}).get("entries", [{}])
            value = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard = wins[0].get("place", "0") if wins and wins[0] else "0"
            return value, leaderboard

        async def losses(self):
            """Returns 'wins' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.losses()\n        print('games lost:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            return value, leaderboard

        async def highest_win_streak_reached(self):
            """Returns 'highest winstreak reached' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.highest_win_streak_reached()\n        print('highest win streak reached:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            highest_winstreak = self.data.get("Highest winstreak reached", {}).get("entries", [{}])
            value = highest_winstreak[0].get("value", "0") if highest_winstreak and highest_winstreak[0] else "0"
            leaderboard = highest_winstreak[0].get("place", "0") if highest_winstreak and highest_winstreak[0] else "0"
            return value, leaderboard
                    
        async def bow_kills(self):
            """Returns 'bow kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.bow_kills()\n        print('killed with bow:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            bow_kills = self.data.get("Bow kills", {}).get("entries", [{}])
            value = bow_kills[0].get("value", "0") if bow_kills and bow_kills[0] else "0"
            leaderboard = bow_kills[0].get("place", "0") if bow_kills and bow_kills[0] else "0"
            return value, leaderboard
                    
        async def arrows_hit(self):
            """Returns 'arrow hit' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.arrow_hit()\n        print('arrow hit:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            arrows_hit = self.data.get("Arrows hit", {}).get("entries", [{}])
            value = arrows_hit[0].get("value", "0") if arrows_hit and arrows_hit[0] else "0"
            leaderboard = arrows_hit[0].get("place", "0") if arrows_hit and arrows_hit[0] else "0"
            return value, leaderboard
                    
        async def kills(self):
            """Returns 'kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kills()\n        print('number of player kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            kills = self.data.get("Kills", {}).get("entries", [{}])
            value = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard = kills[0].get("place", "0") if kills and kills[0] else "0"
            return value, leaderboard
                    
        async def melee_kills(self):
            """Returns 'melee kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.melee_kills()\n        print('melee kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            melee_kills = self.data.get("Melee kills", {}).get("entries", [{}])
            value = melee_kills[0].get("value", "0") if melee_kills and melee_kills[0] else "0"
            leaderboard = melee_kills[0].get("place", "0") if melee_kills and melee_kills[0] else "0"
            return value, leaderboard
                    
        async def deaths(self):
            """Returns 'deaths' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.deaths()\n        print('times died:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            deaths = self.data.get("Deaths", {}).get("entries", [{}])
            value = deaths[0].get("value", "0") if deaths and deaths[0] else "0"
            leaderboard = deaths[0].get("place", "0") if deaths and deaths[0] else "0"
            return value, leaderboard
                    
        async def void_kills(self):
            """Returns 'void kills' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.void_kills()\n        print('void kills:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            void_kills = self.data.get("Void kills", {}).get("entries", [{}])
            value = void_kills[0].get("value", "0") if void_kills and void_kills[0] else "0"
            leaderboard = void_kills[0].get("place", "0") if void_kills and void_kills[0] else "0"
            return value, leaderboard
                    
        async def games_played(self):
            """Returns 'games played' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.games_played()\n        print('games played:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            return value, leaderboard
                    
        async def arrow_shot(self):
            """Returns 'arrow shot' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.arrow_shot()\n        print('number of arrow shot:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            arrows_shot = self.data.get("Arrows shot", {}).get("entries", [{}])
            value = arrows_shot[0].get("value", "0") if arrows_shot and arrows_shot[0] else "0"
            leaderboard = arrows_shot[0].get("place", "0") if arrows_shot and arrows_shot[0] else "0"
            return value, leaderboard

        
    async def Profile(self, player):
        """
        player: str[Any]
        ~~~~~~~~~~~~~~~~
        
        Fetch profile values of a given player.
        Can not be hidden from the API.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:
                if int(resp.status) !=  200:
                    return None
                data = json.loads(await resp.text())

                return self.ProfileContext(data)
            

    async def Stats(self, player: str, gamemode: str, interval: str, mode: str):
        """
        player: str[Any]

        gamemode: Option[opfactions, bedwars, opprison, opskyblock, classicskyblock, survival, kitpvp, practice, skywars, lifesteal]
        
        interval: Option[weekly, yearly, monthly, total]

        mode: Option[
            [BEDWARS: SOLO/DOUBLES/TRIPLES/QUADS/ALL_MODES],
            [SKYWARS: SOLO/DOUBLES/ALL_MODES]
        ]"""

        self.player = player
        self.gamemode = gamemode.lower()
        self.interval = interval.lower()
        self.mode = mode.upper()


        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{self.player}/leaderboard?type={self.gamemode}&interval={self.interval}&mode={self.mode}') as resp:
                if int(resp.status) !=  200:

                    if int(resp.status) ==  400:
                        pass
                    elif int(resp.status) == 404:
                        pass
                    else:
                        pass
                data = json.loads(await resp.text())

                if self.gamemode == 'bedwars':
                    return self._PlayerStats__BEDWARS_(data)
                elif self.gamemode == 'skywars':
                    return self._PlayerStats__SKYWARS_(data)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
