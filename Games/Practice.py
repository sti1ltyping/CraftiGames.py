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
    """
    Wraps RankedPractice
    ~~~~~

    ==================================================================================================

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
    SOFTWARE."""

    def __init__(self, data):
        self.data: dict = data

    async def wins(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
        
    async def wlr(self) -> float:
        """
        Wins is to Losses ratio.

        Returns:
        - Ratio of wins is to losses upto 2 decimal places.
        """
        wins = await self.wins(leaderboard=False)
        losse = await self.losses(leaderboard=False)
        if losse == 0:
            return int(wins)
        else:
            ratio = int(wins) / int(losse)
            return float('{:.2f}'.format(ratio))
        
    async def win_rate(self) -> float:
        """
        Wins rate.

        Returns:
        - Win rate upto 2 decimal places.
        """
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)
        total = wins + losses
        rate = wins/total * 100
        return float('{:.2f}'.format(rate))
    
    async def lose_rate(self) -> float:
        """
        Lose rate.
        
        Returns:
        - Lose rate upto 2 decimal places.
        """
        win_rate = await self.win_rate()
        return 100 - win_rate

    async def kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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

    async def hits_dealt(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
        """
        Get the number of Hits dealt and/or leaderboard position.
        
        Parameters:
        - value (bool): If True, return the number of wins.
        - leaderboard (bool): If True, return the leaderboard position.
            
        Returns:
        - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
        - If only value is True, returns the number of wins.
        - If only leaderboard is True, returns the leaderboard position.
        - If both value and leaderboard are False, returns None.
        """
        hits_dealt = self.data.get("Hits dealt", {}).get("entries", [{}])
        value_result = hits_dealt[0].get("value", "0") if hits_dealt and hits_dealt[0] else "0"
        leaderboard_result = hits_dealt[0].get("place", "0") if hits_dealt and hits_dealt[0] else "0"
            
        if value and leaderboard:
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        
    async def hits_taken(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
        """
        Get the number of hits taken and/or leaderboard position.
        
        Parameters:
        - value (bool): If True, return the number of wins.
        - leaderboard (bool): If True, return the leaderboard position.
        
        Returns:
        - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
        - If only value is True, returns the number of wins.
        - If only leaderboard is True, returns the leaderboard position.
        - If both value and leaderboard are False, returns None.
        """
        hits_taken = self.data.get("Hits taken", {}).get("entries", [{}])
        value_result = hits_taken[0].get("value", "0") if hits_taken and hits_taken[0] else "0"
        leaderboard_result = hits_taken[0].get("place", "0") if hits_taken and hits_taken[0] else "0"
        
        if value and leaderboard:
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        
    async def hit_rate(self) -> float:
        """
        Hit rate.

        Returns:
        - Hit rate upto 2 decimal places.
        """
        hits_dealt = await self.hits_dealt(leaderboard=False)
        hits_taken = await self.hits_taken(leaderboard=False)
        total = hits_dealt + hits_taken
        rate = hits_taken/total * 100
        return float('{:.2f}'.format(rate))
    
    async def hit_taken_rate(self) -> float:
        """
        Hit taken rate.
        
        Returns:
        - Hit taken rate upto 2 decimal places.
        """
        hit_dealt_rate = await self.hit_rate()
        return 100 - hit_dealt_rate

    async def highest_winstreak_reached(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
                
    async def void_kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
        
    async def elo(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
        """
        Get the number of Elo and/or leaderboard position.
        
        Parameters:
        - value (bool): If True, return the number of wins.
        - leaderboard (bool): If True, return the leaderboard position.
        
        Returns:
        - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
        - If only value is True, returns the number of wins.
        - If only leaderboard is True, returns the leaderboard position.
        - If both value and leaderboard are False, returns None.
        """
        elo = self.data.get("Elo", {}).get("entries", [{}])
        value_result = elo[0].get("value", "0") if elo and elo[0] else "0"
        leaderboard_result = elo[0].get("place", "0") if elo and elo[0] else "0"
        
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
        Number of  number of games left `/hub`.

        Returns:
        - Number of games left unplayed.
        """
        gamesplayed = await self.games_played(leaderboard=False)
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)
    
    async def raw(self) -> dict:
        """
        Returns:
        - Raw data.
        """
        return self.data


class Unrankedpractice:
    """
    Wraps UnrankedPractice
    ~~~~~

    ==================================================================================================

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
    SOFTWARE."""
    
    def __init__(self, data):
        self.data: dict = data

    async def wins(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
        
    async def wlr(self) -> float:
        """
        Wins is to Losses ratio.

        Returns:
        - Ratio of wins is to losses upto 2 decimal places.
        """
        wins = await self.wins(leaderboard=False)
        losse = await self.losses(leaderboard=False)
        if losse == 0:
            return int(wins)
        else:
            ratio = int(wins) / int(losse)
            return float('{:.2f}'.format(ratio))
        
    async def win_rate(self) -> float:
        """
        Wins rate.

        Returns:
        - Win rate upto 2 decimal places.
        """
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)
        total = wins + losses
        rate = wins/total * 100
        return float('{:.2f}'.format(rate))
    
    async def lose_rate(self) -> float:
        """
        Lose rate.
        
        Returns:
        - Lose rate upto 2 decimal places.
        """
        win_rate = await self.win_rate() 
        return 100 - win_rate

    async def kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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

    async def hits_dealt(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
        """
        Get the number of Hits dealt and/or leaderboard position.
        
        Parameters:
        - value (bool): If True, return the number of wins.
        - leaderboard (bool): If True, return the leaderboard position.
            
        Returns:
        - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
        - If only value is True, returns the number of wins.
        - If only leaderboard is True, returns the leaderboard position.
        - If both value and leaderboard are False, returns None.
        """
        hits_dealt = self.data.get("Hits dealt", {}).get("entries", [{}])
        value_result = hits_dealt[0].get("value", "0") if hits_dealt and hits_dealt[0] else "0"
        leaderboard_result = hits_dealt[0].get("place", "0") if hits_dealt and hits_dealt[0] else "0"
            
        if value and leaderboard:
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        
    async def hits_taken(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
        """
        Get the number of hits taken and/or leaderboard position.
        
        Parameters:
        - value (bool): If True, return the number of wins.
        - leaderboard (bool): If True, return the leaderboard position.
        
        Returns:
        - If both value and leaderboard are True, returns a tuple of (value, leaderboard).
        - If only value is True, returns the number of wins.
        - If only leaderboard is True, returns the leaderboard position.
        - If both value and leaderboard are False, returns None.
        """
        hits_taken = self.data.get("Hits taken", {}).get("entries", [{}])
        value_result = hits_taken[0].get("value", "0") if hits_taken and hits_taken[0] else "0"
        leaderboard_result = hits_taken[0].get("place", "0") if hits_taken and hits_taken[0] else "0"
        
        if value and leaderboard:
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
        
    async def hit_rate(self) -> float:
        """
        Hit rate.

        Returns:
        - Hit rate upto 2 decimal places.
        """
        hits_dealt = await self.hits_dealt(leaderboard=False)
        hits_taken = await self.hits_taken(leaderboard=False)
        total = hits_dealt + hits_taken
        rate = hits_taken/total * 100
        return float('{:.2f}'.format(rate))
    
    async def hit_taken_rate(self) -> float:
        """
        Hit taken rate.
        
        Returns:
        - Hit taken rate upto 2 decimal places.
        """
        hit_dealt_rate = await self.hit_rate()
        return 100 - hit_dealt_rate

    async def highest_winstreak_reached(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
            ) -> (tuple[int, int] | int | None):
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
                
    async def void_kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            
    async def exploited(self) -> int:
        """
        Number of  number of games left `/hub`.

        Returns:
        - Number of games left unplayed.
        """
        gamesplayed = await self.games_played(leaderboard=False)
        wins = await self.wins(leaderboard=False)
        losses = await self.losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)
    
    async def raw(self) -> dict:
        """
        Returns:
        - Raw data.
        """
        return self.data