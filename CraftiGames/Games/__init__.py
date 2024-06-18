"""
MIT License

Copyright (c) 2024 sti1ltyping

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

class Stats:
    """
    Wraps Bedwars 
    ~~~~~

    ==================================================================================================

    MIT License

    Copyright (c) 2024 sti1ltyping

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

    def __init__(self, data: dict) -> None:
        self.raw: dict = data
    

    def _wins(
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
        wins = self.raw.get("Wins", {}).get("entries", [{}])
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


    def _losses(
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
        Losses = self.raw.get("Losses", {}).get("entries", [{}])
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


    def _wlr(self) -> float:
        """
        Wins is to Losses ratio.

        Returns:
        - Ratio of wins is to losses upto 2 decimal places.
        """
        wins = self._wins(leaderboard=False)
        losse = self._losses(leaderboard=False)
        if losse == 0:
            return int(wins)
        else:
            ratio = int(wins) / int(losse)
            return float('{:.2f}'.format(ratio))


    def _win_rate(self) -> float:
        """
        Wins rate.

        Returns:
        - Win rate upto 2 decimal places.
        """
        wins = self._wins(leaderboard=False)
        losses = self._losses(leaderboard=False)
        total = wins + losses
        if total == 0 and wins == 0:
            return 0
        elif total == 0:
            return 100
        rate = wins/total * 100
        return float('{:.2f}'.format(rate))


    def _lose_rate(self) -> float:
        """
        Lose rate.
        
        Returns:
        - Lose rate upto 2 decimal places.
        """
        win_rate = self._win_rate()
        if win_rate == 0:
            return 0
        return 100 - win_rate


    def _kills(
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
        kills = self.raw.get("Kills", {}).get("entries", [{}])
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


    def _deaths(
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
        deaths = self.raw.get("Deaths", {}).get("entries", [{}])
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


    def _kdr(self) -> float:
        """
        Kills is to Deaths ratio.

        Returns:
        - Ratio of kills is to deaths upto 2 decimal places.
        """
        kills = self._kills(leaderboard=False)
        deaths = self._deaths(leaderboard=False)
        if deaths == 0:
            return int(kills)
        else:
            ratio = int(kills) / int(deaths)
            return float('{:.2f}'.format(ratio))


    def _kill_rate(self) -> float:
        """
        Kill rate.

        Returns:
        - Kill rate upto 2 decimal places.
        """
        kills = self._kills(leaderboard=False)
        deaths = self._deaths(leaderboard=False)
        total = kills + deaths
        if total == 0 and kills == 0:
            return 0
        elif total == 0:
            return 100
        rate = kills/total * 100
        return float('{:.2f}'.format(rate))


    def _death_rate(self) -> float:
        """
        Death rate.
        
        Returns:
        - Death rate upto 2 decimal places.
        """
        kill_rate = self._kill_rate()
        if kill_rate == 0:
            return 0
        return 100 - kill_rate


    def _final_kills(
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
        Finals_deaths = self.raw.get("Final kills", {}).get("entries", [{}])
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


    def _final_deaths(
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
        Finals = self.raw.get("Final deaths", {}).get("entries", [{}])
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


    def _fkdr(self) -> (int | float):
        """
        Final kills is to Final deaths ratio.

        Returns:
        - Ratio of final kills is to final deaths upto 2 decimal places.
        """
        final_kills = self._final_kills(leaderboard=False)
        final_deaths = self._final_deaths(leaderboard=False)
        if final_deaths == 0:
            return int(final_kills)
        else:
            ratio = int(final_kills) / int(final_deaths)
            return float('{:.2f}'.format(ratio))


    def _final_kill_rate(self) -> float:
        """
        Final kill rate.

        Returns:
        - Final kill rate upto 2 decimal places.
        """
        final_kills = self._final_kills(leaderboard=False)
        final_death = self._final_deaths(leaderboard=False)
        total = final_kills + final_death
        if total == 0 and final_kills == 0:
            return 0
        elif total == 0:
            return 100
        rate = final_kills/total * 100
        return float('{:.2f}'.format(rate))


    def _final_death_rate(self) -> float:
        """
        Final death rate.
        
        Returns:
        - Final death rate upto 2 decimal places.
        """
        final_kill_rate = self._final_kill_rate()
        if final_kill_rate == 0:
            return 0
        return 100 - final_kill_rate


    def _beds_destroyed(
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
        beds_destroyed = self.raw.get("Beds destroyed", {}).get("entries", [{}])
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


    def _highest_winstreak_reached(
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
        Winstreak = self.raw.get("Highest winstreak reached",{}).get("entries", [{}])
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


    def _bow_kills(
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
        Bow_kills = self.raw.get("Bow_kills", {}).get("entries", [{}])
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


    def _arrows_shot(
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
        arrows_shot = self.raw.get("Arrows shot", {}).get("entries", [{}])
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


    def _arrows_hit(
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
        arrows_hit = self.raw.get("Arrows hit", {}).get("entries", [{}])
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


    def _ahr(self) -> float:
        """
        Arrow hit ratio.

        Returns:
        - Arrow hit is to arrow shot ratio upto 2 decimal places.
        """
        arrows_hit = self._arrows_hit(leaderboard=False)
        arrows_shot = self._arrows_shot(leaderboard=False)
        if arrows_shot == 0:
            return arrows_hit
        elif arrows_hit == 0:
            return 0
        ratio = arrows_hit/arrows_shot
        return float('{:.2f}'.format(ratio))

        
    def _arrow_hit_rate(self) -> float:
        """
        Arrow hit rate.

        Returns:
        - Arrow hit rate upto 2 decimal places.
        """
        arrows_hit = self._arrows_hit(leaderboard=False)
        arrows_shot = self._arrows_shot(leaderboard=False)
        total = arrows_hit + arrows_shot
        if total == 0 and arrows_hit == 0:
            return 0
        elif total == 0:
            return 100
        rate = arrows_hit/total * 100
        return float('{:.2f}'.format(rate))


    def _arrow_miss_rate(self) -> float:
        """
        Arrow miss rate.
        
        Returns:
        - Arrow miss rate upto 2 decimal places.
        """
        arrow_hit_rate = self._arrow_hit_rate()
        if arrow_hit_rate == 0:
            return 0
        return 100 - arrow_hit_rate
    

    def _hits_dealt(
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
        hits_dealt = self.raw.get("Hits dealt", {}).get("entries", [{}])
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


    def _hits_taken(
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
        hits_taken = self.raw.get("Hits taken", {}).get("entries", [{}])
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


    def _hit_rate(self) -> float:
        """
        Hit rate.

        Returns:
        - Hit rate upto 2 decimal places.
        """
        hits_dealt = self._hits_dealt(leaderboard=False)
        hits_taken = self._hits_taken(leaderboard=False)
        total = hits_dealt + hits_taken
        if total == 0 and hits_dealt == 0:
            return 0
        elif total == 0:
            return 100
        rate = hits_taken/total * 100
        return float('{:.2f}'.format(rate))


    def _hit_taken_rate(self) -> float:
        """
        Hit taken rate.
        
        Returns:
        - Hit taken rate upto 2 decimal places.
        """
        hit_dealt_rate = self._hit_rate()
        if hit_dealt_rate == 0:
            return 0
        return 100 - hit_dealt_rate
    
    
    def _elo(
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
        elo = self.raw.get("Elo", {}).get("entries", [{}])
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


    def _melee_kills(
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
        melee_kills = self.raw.get("Melee kills", {}).get("entries", [{}])
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


    def _void_kills(
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
        void_kills = self.raw.get("Void kills", {}).get("entries", [{}])
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


    def _games_played(
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
        games_played = self.raw.get("Games played", {}).get("entries", [{}])
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


    def _exploited(
            self
            ) -> int:
        """
        Number of  number of games left `/hub`.

        Returns:
        - Number of games left unplayed.
        """
        gamesplayed = self._games_played(leaderboard=False)
        wins = self._wins(leaderboard=False)
        losses = self._losses(leaderboard=False)

        return int(gamesplayed) - int(wins + losses)
