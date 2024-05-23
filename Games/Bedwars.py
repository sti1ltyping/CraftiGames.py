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


class Bedwars:
    """
    Wraps Bedwars 
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

    async def deaths(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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

    async def kdr(self) -> (int | float):
        """
        Kills is to Deaths ratio.

        Returns:
        - Ratio of kills is to deaths upto 2 decimal places.
        """
        kills = await self.kills(leaderboard=False)
        deaths = await self.deaths(leaderboard=False)
        if deaths == 0:
            return int(kills)
        else:
            ratio = int(kills) / int(deaths)
            return float('{:.2f}'.format(ratio))
        
    async def kill_rate(self) -> float:
        """
        Kill rate.

        Returns:
        - Kill rate upto 2 decimal places.
        """
        kills = await self.kills(leaderboard=False)
        deaths = await self.deaths(leaderboard=False)
        total = kills + deaths
        rate = kills/total * 100
        return float('{:.2f}'.format(rate))
    
    async def death_rate(self) -> float:
        """
        Death rate.
        
        Returns:
        - Death rate upto 2 decimal places.
        """
        kill_rate = await self.kill_rate()
        return 100 - kill_rate
        
    async def final_kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
    
    async def final_deaths(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
    
    async def fkdr(self) -> (int | float):
        """
        Final kills is to Final deaths ratio.

        Returns:
        - Ratio of final kills is to final deaths upto 2 decimal places.
        """
        final_kills = await self.final_kills(leaderboard=False)
        final_deaths = await self.final_deaths(leaderboard=False)
        if final_deaths == 0:
            return int(final_kills)
        else:
            ratio = int(final_kills) / int(final_deaths)
            return float('{:.2f}'.format(ratio))
        
    async def final_kill_rate(self) -> float:
        """
        Final kill rate.

        Returns:
        - Final kill rate upto 2 decimal places.
        """
        final_kills = await self.final_kills(leaderboard=False)
        final_death = await self.final_deaths(leaderboard=False)
        total = final_kills + final_death
        rate = final_kills/total * 100
        return float('{:.2f}'.format(rate))
    
    async def final_death_rate(self) -> float:
        """
        Final death rate.
        
        Returns:
        - Final death rate upto 2 decimal places.
        """
        final_kill_rate = await self.final_kill_rate()
        return 100 - final_kill_rate
        
    async def beds_destroyed(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
            return int(value_result), int(leaderboard_result)
        elif value:
            return int(value_result)
        elif leaderboard:
            return int(leaderboard_result)
        else:
            return None
    
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
        
    async def arrows_shot(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
    
    async def arrows_hit(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
        
    async def ahr(self) -> float:
        """
        Arrow hit ratio.

        Returns:
        - Arrow hit is to arrow shot ratio upto 2 decimal places.
        """
        arrows_hit = await self.arrows_hit()
        arrows_shot = await self.arrows_shot()
        ratio = arrows_hit/arrows_shot
        return float('{:.2f}'.format(ratio))

        
    async def arrow_hit_rate(self) -> float:
        """
        Arrow hit rate.

        Returns:
        - Arrow hit rate upto 2 decimal places.
        """
        arrows_hit = await self.arrows_hit(leaderboard=False)
        arrows_shot = await self.arrows_shot(leaderboard=False)
        total = arrows_hit + arrows_shot
        rate = arrows_hit/total * 100
        return float('{:.2f}'.format(rate))
    
    async def arrow_miss_rate(self) -> float:
        """
        Arrow miss rate.
        
        Returns:
        - Arrow miss rate upto 2 decimal places.
        """
        arrow_hit_rate = await self.arrow_hit_rate()
        return 100 - arrow_hit_rate
    
    async def melee_kills(
            self,
            value: bool = True,
            leaderboard: bool = True
            ) -> (tuple[int, int] | int | None):
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
        
    async def exploited(
            self
            ) -> int:
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