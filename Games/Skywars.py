"""
MIT License

Copyright (c) 2024 Sti1lTyping

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None

    async def kdr(self) -> (int | float):
        """Returns 'kdr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

        kills = await self.kills(leaderboard=False)
        deaths = await self.deaths(leaderboard=False)
        if deaths == "0":
            return int(kills)
        else:
            ratio = int(kills) / int(deaths)
            return float('{:.2f}'.format(ratio))
        
    async def wlr(self) -> (int | float):
        """Returns 'wlr' block.\n\nTo extract:\n~~~~\n\n~~~\nfrom PikaPY import Pikanetwork\nimport asyncio\n\nasync def example():\n    client = await Pikanetwork().Stats(player='Example', gamemode='skywars', interval='weekly', mode='all_modes')\n    if client:\n        value, leaderboard = await client.kdr()\n        print('kdr:', value, 'leaderboard:', leaderboard)\n    else:\n        print('Failed to get response')\n\nasyncio.run(example())"""

        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)
        if losses == "0":
            return int(wins)
        else:
            ratio = int(wins) / int(losses)
            return float('{:.2f}'.format(ratio))
        
    async def exploited(self) -> int:

        """
        Get the number of games left (/hub).
        """

        gamesplayed = await self.games_played(leaderboard=False)
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)