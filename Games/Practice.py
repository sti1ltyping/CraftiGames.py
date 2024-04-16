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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        

    async def exploited(self) -> int:

        """
        Get the number of games left (/hub).
        """

        gamesplayed = await self.games_played(leaderboard=False)
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)
    
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        
    
    async def exploited(self) -> int:

        """
        Get the number of games left (/hub).
        """

        gamesplayed = await self.games_played(leaderboard=False)
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)