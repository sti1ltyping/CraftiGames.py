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

from PikaPY.Games import Stats # type: ignore

class Skywars:
    """
    Wraps Skywars
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
    
    def __init__(self, data: dict):
        self.raw: dict = data
        self.__stats__: Stats = Stats(self.raw)

    @property
    def wins(self) -> int:
        """
        Returns
        - Number of wins. (int)
        """
        return self.__stats__._wins(
            value=True,
            leaderboard=False
        )

    @property
    def wins_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of wins. (int)
        """
        return self.__stats__._wins(
            value=False,
            leaderboard=True
        )

    @property
    def losses(self) -> int:
        """
        Returns
        - Number of losses. (int)
        """
        return self.__stats__._losses(
            value=True,
            leaderboard=False
        )

    @property
    def losses_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of losses. (int)
        """
        return self.__stats__._losses(
            value=False,
            leaderboard=True
        )

    @property
    def wlr(self) -> float:
        """
        Returns
        - Wins is to losses ratio. (float)
        """
        return self.__stats__._wlr()

    @property
    def win_rate(self) -> float:
        """
        Returns
        - Win rate, calculated using previous wins & losses. (float)
        """
        return self.__stats__._win_rate()

    @property
    def lose_rate(self) -> float:
        """
        Returns
        - Lose rate, calculated using previous wins & losses. (float)
        """
        return self.__stats__._lose_rate()

    @property
    def kills(self) -> int:
        """
        Returns
        - Number of kills. (int)
        """
        return self.__stats__._kills(
            value=True,
            leaderboard=False
        )

    @property
    def kills_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of kills. (int)
        """
        return self.__stats__._kills(
            value=False,
            leaderboard=True
        )

    @property
    def deaths(self) -> int:
        """
        Returns
        - Number of deaths. (int)
        """
        return self.__stats__._deaths(
            value=True,
            leaderboard=False
        )

    @property
    def deaths_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of deaths. (int)
        """
        return self.__stats__._deaths(
            value=False,
            leaderboard=True
        )

    @property
    def kdr(self) -> int:
        """
        Returns
        - Kill is to death ratio. (float)
        """
        return self.__stats__._kdr()

    @property
    def kill_rate(self) -> float:
        """
        Returns
        - kill rate, calculated using previous kills & deaths. (float)
        """
        return self.__stats__._kill_rate()

    @property
    def death_rate(self) -> float:
        """
        Returns
        - death rate, calculated using previous kills & deaths. (float)
        """
        return self.__stats__._death_rate()

    @property
    def highest_winstreak_reached(self) -> int:
        """
        Returns
        - highest winsteak reached. (int)
        """
        return self.__stats__._highest_winstreak_reached(
            value=True,
            leaderboard=False
        )
    
    @property
    def highest_winstreak_reached_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on highest winstreak. (int)
        """
        return self.__stats__._highest_winstreak_reached(
            value=False,
            leaderboard=True
        )

    @property
    def bow_kills(self) -> int:
        """
        Returns
        - Number of bow kills. (int)
        """
        return self.__stats__._bow_kills(
            value=True,
            leaderboard=False
        )

    @property
    def bow_kills_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of bow kills. (int)
        """
        return self.__stats__._bow_kills(
            value=False,
            leaderboard=True
        )

    @property
    def arrows_shot(self) -> int:
        """
        Returns
        - Number of arrows shot. (int)
        """
        return self.__stats__._arrows_shot(
            value=True,
            leaderboard=False
        )

    @property
    def arrows_shot_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of arrows shot. (int)
        """
        return self.__stats__._arrows_shot(
            value=False,
            leaderboard=True
        )

    @property
    def arrows_hit(self) -> int:
        """
        Returns
        - Number of arrows hit. (int)
        """
        return self.__stats__._arrows_hit(
            value=True,
            leaderboard=False
        )

    @property
    def arrows_hit_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of arrows hit. (int)
        """
        return self.__stats__._arrows_hit(
            value=False,
            leaderboard=True
        )

    @property
    def ahr(self) -> float:
        """
        Returns
        - Arrow hit ratio. (float)
        """
        return self.__stats__._ahr()

    @property
    def arrow_hit_rate(self) -> float:
        """
        Returns
        - Arrow hit rate, calculated using previous arrows shot & arrows hit. (float)
        """
        return self.__stats__._arrow_hit_rate()

    @property
    def arrow_miss_rate(self) -> float:
        """
        Returns
        - Arrow miss rate, calculated using previous arrows shot & arrows hit. (float)
        """
        return self.__stats__._arrow_miss_rate()

    @property
    def melee_kills(self) -> int:
        """
        Returns
        - Number of melee kills. (int)
        """
        return self.__stats__._melee_kills(
            value=True,
            leaderboard=False
        )

    @property
    def melee_kills_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of melee kills. (int)
        """
        return self.__stats__._melee_kills(
            value=False,
            leaderboard=True
        )

    @property
    def games_played(self) -> int:
        """
        Returns
        - Number of games played. (int)
        """
        return self.__stats__._games_played(
            value=True,
            leaderboard=False
        )

    @property
    def games_played_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of games played. (int)
        """
        return self.__stats__._games_played(
            value=False,
            leaderboard=True
        )

    @property
    def void_kills(self) -> int:
        """
        Returns
        - Number of void kills. (int)
        """
        return self.__stats__._void_kills(
            value=True,
            leaderboard=False
        )

    @property
    def void_kills_lb(self) -> int:
        """
        Returns
        - Leaderboard position based on number of void kills. (int)
        """
        return self.__stats__._void_kills(
            value=False,
            leaderboard=True
        )

    @property
    def exploited(self) -> int:
        """
        Number of number of games left `/hub`.

        Returns:
        - Number of games left unplayed.
        """
        return self.__stats__._exploited()