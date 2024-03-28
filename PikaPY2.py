import aiohttp
import json
import asyncio
from datetime import datetime, timedelta

from typing_extensions import Union, Coroutine

API_requests = 0
last_request_time = datetime.now()

async def avoid_rate_limits():
    """
    Check if the rate limit has been reached,
    and introduce a delay if necessary.
    """
    global API_requests, last_request_time
    current_time = datetime.now()
    time_difference = current_time - last_request_time

    if API_requests >= 10 and time_difference <= timedelta(seconds=1):
        remaining_time = (timedelta(seconds=1) - time_difference).total_seconds()
        await asyncio.sleep(remaining_time)

        API_requests = 0
        last_request_time = datetime.now()

    last_request_time = current_time


class Pikanetwork():
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~


    A basic wrapper for the PikaNetwork's API.
    """

    class weekly:
        interval = 'weekly'
    class monthly:
        interval = 'monthly'
    class yearly:
        interval = 'yearly'
    class total:
        interval = 'total'

    class all_modes:
        mode = 'all_modes'
    class solo:
        mode = 'solo'
    class doubles:
        mode = 'doubles'
    class triples:
        mode = 'triples'
    class quad:
        mode = 'quad'
    

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

        async def connections(self):
            """Returns status of discord account, server boosting and email connection"""
            return self.data.get("discord_verified"), self.data.get("discord_boosting"), self.data.get("email_verified")

        async def username(self):
            """Returns username of the player.\n~~~"""
            return self.data.get("username")
        
        async def level(self) -> str:
            """Returns current level of the player.\n~~~"""
            return self.data.get("rank", {}).get("level")
        
        async def level_percentage(self) -> float:
            """Returns level percentage."""
            return float(self.data.get("rank", {}).get("percentage", 0))
        
        async def highest_minigame_rank(self):
            """Returns highest minigame rank of the player.\n~~~"""
            sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
                "developer": 0, "admin": 1,"manager": 2, "srmod": 3, "moderator": 4, "helper": 5, "trial": 6, "youtuber": 7, "champion": 8, "titan": 9, "elite": 10, "vip": 11
            }.get(x.get('displayName', '').lower(), float('inf')))
            check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
            if check.lower() in ["developer", "admin", "manager", "srmod", "moderator", "helper", "trial", "youtuber", "champion", "titan", "elite", "vip"]:
                return check
            else:
                return 'Unranked'
        
        async def highest_practice_rank(self):
            """Returns highest practice rank of the player.\n~~~"""
            sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
                "emerald": 0,"diamond": 1, "gold": 2, "silver": 3
            }.get(x.get('displayName', '').lower(), float('inf')))
            check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
            if check.lower() in ["emerald","diamond", "gold", "silver"]:
                return check
            else:
                return 'Unranked'
        
        async def last_seen(self) -> int:
            """Returns last seen value discord format."""
            last_seen_raw = self.data.get("lastSeen")
            last_seen = str(last_seen_raw)[:-3]
            return int(last_seen)
        
        async def friend_list(self):
            """Return a list of player's friends. NOTE: Return None if no friends found!"""
            friends_raw = self.data.get('friends', [])
            friends = [user['username'] for user in friends_raw]

            if not friends_raw:
                return None
            return friends
        
        async def friend_count(self):
            """Return number of friend(s). NOTE: Return None if no friends found!"""
            frineds = self.data.get('friends', [])
            if not frineds:
                return None
            return int(len(frineds))
        
        async def guild(self):
            """Fetch guild of the player.\n~~~\n\nreturn None if guild is not found:\n~~~"""
            if "clan" in self.data and self.data["clan"] is None:
                return None
            
            guild_data = self.data.get("clan", {})
            return Pikanetwork().__Client_Guild_Profile__(guild_data)
        

    class Bedwars:
        def __init__(self, data):
            self.data = data

        async def wins(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of wins and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            wins = self.data.get("Wins", {}).get("entries", [{}])
            value_result = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard_result = wins[0].get("place", "0") if wins and wins[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def losses(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of losses and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value_result = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard_result = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def wlr(self):
            """Returns 'wlr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        wlr = await client.wlr()\n        print('wlr:', wlr)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            wins, _ = await self.wins()
            losse, _ = await self.losses()
            if losse == "0":
                return int(wins)
            else:
                ratio = int(wins) / int(losse)
                return float('{:.2f}'.format(ratio))

        async def kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """

            kills = self.data.get("Kills", {}).get("entries", [{}])
            value_result = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard_result = kills[0].get("place", "0") if kills and kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def deaths(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of deaths and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            deaths = self.data.get("Deaths", {}).get("entries", [{}])
            value_result = deaths[0].get("value", "0") if deaths and deaths[0] else "0"
            leaderboard_result = deaths[0].get("place", "0") if deaths and deaths[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def kdr(self) -> (int | float):
            """Returns 'kdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            kills = await self.kills(leaderboard=False)
            deaths = await self.deaths(leaderboard=False)
            if deaths == "0":
                return int(kills)
            else:
                ratio = int(kills) / int(deaths)
                return float('{:.2f}'.format(ratio))
            
        async def final_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of final kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Finals_deaths = self.data.get("Final kills", {}).get("entries", [{}])
            value_result = Finals_deaths[0].get("value", "0") if Finals_deaths and Finals_deaths[0] else "0"
            leaderboard_result = Finals_deaths[0].get("place", "0") if Finals_deaths and Finals_deaths[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def final_deaths(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of final deaths and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Finals = self.data.get("Final deaths", {}).get("entries", [{}])
            value_result = Finals[0].get("value", "0") if Finals and Finals[0] else "0"
            leaderboard_result = Finals[0].get("place", "0") if Finals and Finals[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def fkdr(self) -> (int | float):
            """Returns 'fkdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='bedwars', interval='weekly', mode='all_modes')\n    if client:\n        fkdr = await client.fkdr()\n        print('fkdr:', fkdr)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            final_kills = await self.final_kills(leaderboard=False)
            final_deaths = await self.final_deaths(leaderboard=False)
            if final_deaths == "0":
                return int(final_kills)
            else:
                ratio = int(final_kills) / int(final_deaths)
                return float('{:.2f}'.format(ratio))
            
        async def bed_destroyed(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of beds destroyed and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            beds_destroyed = self.data.get("Beds destroyed", {}).get("entries", [{}])
            value_result = beds_destroyed[0].get("value", "0") if beds_destroyed and beds_destroyed[0] else "0"
            leaderboard_result = beds_destroyed[0].get("place", "0") if beds_destroyed and beds_destroyed[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def highest_win_streak_reached(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of heighest win streak and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Winstreak = self.data.get("Highest winstreak reached",{}).get("entries", [{}])
            value_result = Winstreak[0].get("value", "0") if Winstreak and Winstreak[0] else "0"
            leaderboard_result = Winstreak[0].get("place", "0") if Winstreak and Winstreak[0] else "0"

            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def bow_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of bow kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Bow_kills = self.data.get("Bow_kills", {}).get("entries", [{}])
            value_result = Bow_kills[0].get("value", "0") if Bow_kills and Bow_kills[0] else "0"
            leaderboard_result = Bow_kills[0].get("place", "0") if Bow_kills and Bow_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def games_played(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of games played and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value_result = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard_result = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def arrow_hit(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of arrow hit and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            arrows_hit = self.data.get("Arrows hit", {}).get("entries", [{}])
            value_result = arrows_hit[0].get("value", "0") if arrows_hit and arrows_hit[0] else "0"
            leaderboard_result = arrows_hit[0].get("place", "0") if arrows_hit and arrows_hit[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def melee_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of melee kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            melee_kills = self.data.get("Melee kills", {}).get("entries", [{}])
            value_result = melee_kills[0].get("value", "0") if melee_kills and melee_kills[0] else "0"
            leaderboard_result = melee_kills[0].get("place", "0") if melee_kills and melee_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def void_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of void kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            void_kills = self.data.get("Void kills", {}).get("entries", [{}])
            value_result = void_kills[0].get("value", "0") if void_kills and void_kills[0] else "0"
            leaderboard_result = void_kills[0].get("place", "0") if void_kills and void_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        

    class Skywars:
        def __init__(self, data):
            self.data = data

        async def wins(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of wins and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            wins = self.data.get("Wins", {}).get("entries", [{}])
            value_result = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard_result = wins[0].get("place", "0") if wins and wins[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def losses(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of losses and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value_result = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard_result = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def highest_win_streak_reached(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of highest win streak and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            highest_winstreak = self.data.get("Highest winstreak reached", {}).get("entries", [{}])
            value_result = highest_winstreak[0].get("value", "0") if highest_winstreak and highest_winstreak[0] else "0"
            leaderboard_result = highest_winstreak[0].get("place", "0") if highest_winstreak and highest_winstreak[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def bow_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of bow kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            bow_kills = self.data.get("Bow kills", {}).get("entries", [{}])
            value_result = bow_kills[0].get("value", "0") if bow_kills and bow_kills[0] else "0"
            leaderboard_result = bow_kills[0].get("place", "0") if bow_kills and bow_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def arrows_hit(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of arrow hit and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            arrows_hit = self.data.get("Arrows hit", {}).get("entries", [{}])
            value_result = arrows_hit[0].get("value", "0") if arrows_hit and arrows_hit[0] else "0"
            leaderboard_result = arrows_hit[0].get("place", "0") if arrows_hit and arrows_hit[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            kills = self.data.get("Kills", {}).get("entries", [{}])
            value_result = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard_result = kills[0].get("place", "0") if kills and kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def melee_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of melee kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            melee_kills = self.data.get("Melee kills", {}).get("entries", [{}])
            value_result = melee_kills[0].get("value", "0") if melee_kills and melee_kills[0] else "0"
            leaderboard_result = melee_kills[0].get("place", "0") if melee_kills and melee_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def deaths(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of deaths and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            deaths = self.data.get("Deaths", {}).get("entries", [{}])
            value_result = deaths[0].get("value", "0") if deaths and deaths[0] else "0"
            leaderboard_result = deaths[0].get("place", "0") if deaths and deaths[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def void_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of void kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            void_kills = self.data.get("Void kills", {}).get("entries", [{}])
            value_result = void_kills[0].get("value", "0") if void_kills and void_kills[0] else "0"
            leaderboard_result = void_kills[0].get("place", "0") if void_kills and void_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def games_played(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of games played and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value_result = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard_result = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def arrow_shot(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of arrow shot and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            arrows_shot = self.data.get("Arrows shot", {}).get("entries", [{}])
            value_result = arrows_shot[0].get("value", "0") if arrows_shot and arrows_shot[0] else "0"
            leaderboard_result = arrows_shot[0].get("place", "0") if arrows_shot and arrows_shot[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None

        async def kdr(self):
            """Returns 'kdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            kills = await self.kills(leaderboard=False)
            deaths = await self.deaths(leaderboard=False)
            if deaths == "0":
                return int(kills)
            else:
                ratio = int(kills) / int(deaths)
                return float('{:.2f}'.format(ratio))
            
        async def wlr(self):
            """Returns 'wlr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

            wins = await self.wins(leaderboard=False)
            losses = await self.losses(leaderboard=False)
            if losses == "0":
                return int(wins)
            else:
                ratio = int(wins) / int(losses)
                return float('{:.2f}'.format(ratio))
    

    class Rankedpractice:
        def __init__(self, data):
            self.data = data

        async def wins(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of wins and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """

            wins = self.data.get("Wins", {}).get("entries", [{}])
            value_result = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard_result = wins[0].get("place", "0") if wins and wins[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def losses(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of losses and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """

            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value_result = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard_result = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            kills = self.data.get("Kills", {}).get("entries", [{}])
            value_result = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard_result = kills[0].get("place", "0") if kills and kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def bow_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of bow kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            bow_kills = self.data.get("Bow kills", {}).get("entries", [{}])
            value_result = bow_kills[0].get("value", "0") if bow_kills and bow_kills[0] else "0"
            leaderboard_result = bow_kills[0].get("place", "0") if bow_kills and bow_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def games_played(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of games played and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value_result = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard_result = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def highest_win_streak_reached(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of heighest win streak and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            highest_winstreak = self.data.get("Highest winstreak reached", {}).get("entries", [{}])
            value_result = highest_winstreak[0].get("value", "0") if highest_winstreak and highest_winstreak[0] else "0"
            leaderboard_result = highest_winstreak[0].get("place", "0") if highest_winstreak and highest_winstreak[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
    class Unrankedpractice:
        def __init__(self, data):
            self.data = data

        async def wins(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of wins and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """

            wins = self.data.get("Wins", {}).get("entries", [{}])
            value_result = wins[0].get("value", "0") if wins and wins[0] else "0"
            leaderboard_result = wins[0].get("place", "0") if wins and wins[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def losses(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of losses and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """

            Losses = self.data.get("Losses", {}).get("entries", [{}])
            value_result = Losses[0].get("value", "0") if Losses and Losses[0] else "0"
            leaderboard_result = Losses[0].get("place", "0") if Losses and Losses[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            kills = self.data.get("Kills", {}).get("entries", [{}])
            value_result = kills[0].get("value", "0") if kills and kills[0] else "0"
            leaderboard_result = kills[0].get("place", "0") if kills and kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
                    
        async def bow_kills(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of bow kills and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            bow_kills = self.data.get("Bow kills", {}).get("entries", [{}])
            value_result = bow_kills[0].get("value", "0") if bow_kills and bow_kills[0] else "0"
            leaderboard_result = bow_kills[0].get("place", "0") if bow_kills and bow_kills[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def games_played(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of games played and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            games_played = self.data.get("Games played", {}).get("entries", [{}])
            value_result = games_played[0].get("value", "0") if games_played and games_played[0] else "0"
            leaderboard_result = games_played[0].get("place", "0") if games_played and games_played[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
        
        async def highest_win_streak_reached(
                self,
                value: bool = True,
                leaderboard: bool = True
                ):
            """
            Get the number of heighest win streak and/or leaderboard position.
            
            Parameters:
            - value (bool): If True, return the number of wins.
            - leaderboard (bool): If True, return the leaderboard position.
            
            Returns:
            - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
            - If only value is True, returns the number of wins.
            - If only leaderboard is True, returns the leaderboard position.
            - If both value and leaderboard are False, returns None.
            """
            highest_winstreak = self.data.get("Highest winstreak reached", {}).get("entries", [{}])
            value_result = highest_winstreak[0].get("value", "0") if highest_winstreak and highest_winstreak[0] else "0"
            leaderboard_result = highest_winstreak[0].get("place", "0") if highest_winstreak and highest_winstreak[0] else "0"
            
            if value and leaderboard:
                return value_result, leaderboard_result
            elif value:
                return value_result
            elif leaderboard:
                return leaderboard_result
            else:
                return None
            
    
    class GuildContext:
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
        
        async def created_at(self):
            """Return timestamp of guild created at.\n~~~"""
            return f"{int(datetime.timestamp(datetime.fromisoformat(self.data.get('creationTime', 0))))}"

        async def member_list(self) -> list:
            """Returns guild members [LIST].\n~~~"""
            members = self.data.get("members", [])
            list = []
            for member in members:
                member_stats = member["user"]["username"]
                list.append(member_stats)
            return list 
        
        async def member_count(self) -> int:
            """Returns member count of the guild.\n~~~"""
            members = self.data.get("members", [])
            list = []
            for member in members:
                member_stats = member["user"]["username"]
                list.append(member_stats)
            return int(len(list))
        
        async def raw(self):
            """Return data"""
            return self.data

        
    async def Profile(
            self,
            player: str
            ) -> (ProfileContext | None):
        """
        Profile API
        ~~~~~~~~~

        Parameters:
            - player (str): Ingame name of the player.
            
            Returns:
            - If player is found returs minigame.
            - Retunrs None if unable to find player.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(playerING: str):
            
            API = Pikanetwork()
            player = await API.Profile(playerIGN)

            if player is None:
                return 'Player is not registered on Pikanetwork'
            
            username = await player.username()
            level = await player.level()
            minigame_rank = await player.heighest_minigame_rank()
            practice_rank = await player.heighest_practice_rank()
            
            guild = await player.guild()
            if guild is None:
                return 'Player is not in a guild'
            
            guild_name = await guild.name()
            
            # and many more...

            print(usename, level, minigame_rank, practice_rank, guild_name)
        
        asyncio.run(Example(playerING='AnyPlayer'))
        """
        global API_requests
        API_requests += 1
        await avoid_rate_limits()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:
                if int(resp.status) !=  200:
                    return None
                data = json.loads(await resp.text())

                return self.ProfileContext(data)
            

    async def Stats(
            self,
            player: str,
            gamemode: Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice],
            interval: Union[weekly, monthly, yearly, total],
            mode: Union[all_modes, solo, doubles, triples, quad]
            ) -> (Bedwars | Skywars | Unrankedpractice | Rankedpractice | None):
        """
        Stats API
        ~~~~~~~~~

        Parameters:
            - player (str): Ingame name of the player.
            - gamemode (Union): minigame of the stats.
            - interval (Union): Timespan of the stats.
            - mode (Union): mode of the minigames.
            
            Returns:
            - If player is found returs minigame.
            - Retunrs None if unable to find player.

            Raise:
            - Error if gamemode, interval or mode is invalid.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(playerING: str):
            
            API = Pikanetwork()
            player = await API.Stats(playerIGN, 'bedwars', 'weekly', 'all_modes')

            if player is None:
                return 'Player is hidden from the API'
            
            wins = await player.wins(leaderboard=False)
            losses, losses_leaderboard = await player.losses()
            wlr = await player.wlr()
            final_kills_leadeboard = await player.final_kills(value=False)
            
            # and many more...

            print(wins, losses, losses_leaderboard, wlr, final_kills_leaderboard)
        
        asyncio.run(Example(playerING='AnyPlayer'))
        """

        self.player: str = player
        self.gamemode: str = gamemode.lower()
        self.interval: str = interval.lower()
        self.mode: str = mode.upper()

        global API_requests
        API_requests += 1
        await avoid_rate_limits()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{self.player}/leaderboard?type={self.gamemode}&interval={self.interval}&mode={self.mode}') as resp:

                if int(resp.status) !=  200: # Couldn't find the player

                    # Invalid args
                    if self.gamemode.lower() not in ['bedwars', 'skywars', 'unrankedpractice', 'rankedpractice']:
                        raise ValueError('Invalid gamemode has been passed, please use one of the following\n-> bedwars\n-> skywars\n-> unrankedpractice\n-> rankedpractice')
                    elif self.interval.lower() not in ['weekly', 'monthly', 'yearly', 'total']:
                        raise ValueError('Invalid interval has been passed, please use one of the following\n-> weekly\n-> monthly\n-> yearly\n-> total')
                    elif self.mode.lower() not in ['all_modes', 'solo', 'doubles', 'triples', 'quad']:
                        raise ValueError('Invalid mode has been passed, please use one of the following\n-> all_modes\n-> solo\n-> doubles\n-> triples\n-> quad')
                    
                    # Player is not registered in the PikaNetwork database
                    else:
                        return None 
                        
                data = json.loads(await resp.text())

                if self.gamemode == 'bedwars':
                    return self.Bedwars(data)
                elif self.gamemode == 'skywars':
                    return self.Skywars(data)
                elif self.gamemode == 'unrankedpractice':
                    return self.Unrankedpractice(data)
                elif self.gamemode == 'rankedpractice':
                    return self.Rankedpractice(data)
                
    
    async def Guild(
            self,
            guild: str
            ) -> (GuildContext | None):
        """
        Guild API
        ~~~~~~~~~

        Parameters:
            - guild (str): Name of the guild.
            
            Returns:
            - If guild is found returns GuildContext.
            - Retunrs None if unable to find guild.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(guild: str):
            
            API = Pikanetwork()
            guild = await API.Guild(guild)

            if guild is None:
                return 'Invalid guild name has been passed!'
            
            name = await guild.name()
            tag = await guild.tag()
            lvl = await guild.level()
            leader = await guild.owner()
            member_count = await guild.member_count()
            member_list = await guild.member_list()

            print(name, tag, lvl, leader, member_count, member_list)
        
        asyncio.run(Example(guild='AnyGuild'))
        """

        global API_requests
        API_requests += 1
        await avoid_rate_limits()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/clans/{guild}') as resp:
                if int(resp.status) !=  200:
                    return None
                
                data = json.loads(await resp.text())
                return self.GuildContext(data)
