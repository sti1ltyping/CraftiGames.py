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

from .utils import (
    Weekly as Weekly,
    Monthly as Monthly,
    Yearly as Yearly,
    Total as Total,
    
    All_Modes as All_Modes,
    Solo as Solo,
    Doubles as Doubles,
    Triples as Triples,
    Quadriples as Quadriples
)

from .utils import packages

from .utils import (
    Gamemodes as Gamemodes,
    Intervals as Intervals,
    Modes as Modes
)

from .utils import header

from .RefactorAPI.Guilds import Guild
from .RefactorAPI.Profiles import PikaProfile
from .RefactorAPI.Leaderboard import CombinedLeaderboard
from .RefactorAPI.NetworkStatus import NetworkStatus
from .RefactorAPI.Recaps import Recap

from .Games.Bedwars import Bedwars
from .Games.Skywars import Skywars
from .Games.Practice import Unrankedpractice, Rankedpractice

from .Punishments import History

from .Ratelimits import PikaNetworkRateLimitHandler as RateLimits

from .ResponseError import faulty

from ._Logger import log

from .utils import Check, Missing

from .utils import (
    APIBlockedException,
    APIResponseError,
    Do_Not_Touch
)

from typing import (
    Union, Literal, List, Tuple
)


class PikaAnnotations:
    """
    Helper class
    ~~~~~~~~
    =============

    - Represents `TypeAnnotation` for PikaNetwork's API wrapper.
    """
    Stats             =      Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]  |     None      | Missing
    Profile           =      PikaProfile                                                |     None      | Missing
    Guild             =      Guild                                                      |     None      | Missing
    Punishments       =      History                                                    |     None      | Missing
    Status            =      NetworkStatus                                              |     None      | Missing
    Recap             =      Recap                                                      |     None      | Missing

    Pikanetwork       :      'Pikanetwork'                             =     None, ..., None, ..., None | Missing
    PikaAnnotations   :      'PikaAnnotations'                         =     None, ..., None, ..., None | Missing


class Pikanetwork:
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~
    A basic wrapper for the PikaNetwork's API.

    =============================

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

    def __init__(self, *, session: packages.aiohttp.ClientSession = ...) -> None:
        self.session = session
        self.cache = {...}

    async def __aenter__(self):
        if self.session == Ellipsis:
            self.session = packages.aiohttp.ClientSession(headers = await header())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session and self.session != ...:
            await self.session.close()

    
    class PikaAnnotations:
        """
        Helper class
        ~~~~~~~~
        =============

        - Represents `TypeAnnotation` for PikaNetwork's API wrapper.
        """
        Stats             =      Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]  |     None      | Missing
        Profile           =      PikaProfile                                                |     None      | Missing
        Guild             =      Guild                                                      |     None      | Missing
        Punishments       =      History                                                    |     None      | Missing
        Status            =      NetworkStatus                                              |     None      | Missing
        Recap             =      Recap                                                      |     None      | Missing

        Pikanetwork       :      'Pikanetwork'                             =     None, ..., None, ..., None | Missing
        PikaAnnotations   :      'PikaAnnotations'                         =     None, ..., None, ..., None | Missing


    async def Profile(
            self,
            player: str,
            **kwargs: Missing
            ) -> Union[PikaProfile, None]:
        """
        :Profile API: Fetches profile data of a user.
        

        Parameters:
            - player (str) : In game name of the player.
            
        Returns:
            - If player is found returns `PikaProfile`, which can be further extracted.
            - `None` if unable to find player.

        Raise:
            - `APIBlockedException` if request is getting blocked.
            - `APIResponseError` if API isn't responding.
        
        
        :Example: https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/Profile.py 
        """

        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config

        await RateLimits.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:

            status = resp.status

            if status == 200:
                return PikaProfile(await resp.json(), session=self.session)

            elif status == 429 and Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Profile(player)

            elif status == 400 or status == 204 or status == 404:
                packages.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass
   

    async def Stats(
            self,
            player: str,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            **kwargs: Missing
            ) -> Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice, None]:
        """
        Stats API
        ~~~~~~~~~

        Parameters:
            - player (str) : Ingame name of the player.
            - gamemode (Literal) : minigame of the stats.
            - interval (Literal) : Timespan of the stats.
            - mode (Literal) : mode of the minigames.
            
        Returns:
            - If player is found returns minigame.
            - Returns None if unable to find player.

        Raise:
            - `ValueError` if gamemode, interval or mode is invalid.
            - `APIBlockedException` if request is getting blocked.
            - `APIResponseError` if API isn't responding.
        
        :Example: https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/Stats.py
        """
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config

        if Recursion <= 0:
            player, gamemode, interval, mode = str(player), gamemode.lower(), interval.lower(), mode.upper()
            Check().__stats_input__(gamemode, interval, mode)

        await RateLimits.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:

            status = resp.status

            if status == 200:
                data: dict = await resp.json()

                if await faulty(data) and Recursion <= config.allowed_recursion:
                    Recursion += 1
                    packages.asyncio.create_task(log('Faulty Stats detected: ', Recursion, 'X'))
                    return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)

                return {
                    'bedwars': Bedwars,
                    'skywars': Skywars,
                    'unrankedpractice': Unrankedpractice,
                    'rankedpractice': Rankedpractice
                }.get(
                    gamemode,
                    lambda x: None
                )(data)


            elif status == 429 and Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)
            
            elif status == 204:
                packages.asyncio.create_task(log(player, ' is hidden from the API!'))
                return None
            
            elif status == 400 or status == 404:
                packages.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass


    async def Guild(
            self,
            guild: str,
            **kwargs: Missing
            ) -> Union[Guild, None]:
        """
        Guild API
        ~~~~~~~~~

        Parameters:
            - guild (str) : Name of the guild.
        
        Returns:
            - If guild is found returns `GuildContext`.
            - Returns `None` if unable to find guild.

        Raise:
            - `APIBlockedException` if request is getting blocked.
            - `APIResponseError` if API isn't responding.

        :Example: https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/Guild.py
        """
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config

        await RateLimits.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/clans/{guild}') as resp:

            status = resp.status

            if status == 200:
                return Guild(await resp.json())
            
            elif status == 429 and Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Guild(guild)
            
            elif status == 400 or status == 204  or status == 404:
                packages.asyncio.create_task(log(guild, ' not found!'))
                return None
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass


    async def __leaderboard__helper__(
            self,
            gamemode,
            stats,
            interval,
            mode,
            offset: int,
            limit: int,
            **kwargs
        ) -> Union[dict, None]:
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config
        await RateLimits.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/leaderboards?type={gamemode}&stat={stats}&interval={interval}&mode={mode}&offset={offset}&limit={limit}') as resp:
            
            status = resp.status

            if status == 200:
                return await resp.json()
            
            elif status == 429 and Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, limit, Recursion=Recursion)
            
            elif status == 400 or status == 204  or status == 404:
                return None
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass


    async def Leaderboard(
            self,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            stats: Literal['wins', 'losses', 'kills', 'deaths', 'final_kills', 'final_deaths', 'bed_destroyed', 'melee_kills', 'void_kills', 'bow_kills', 'arrows_hit', 'arrows_shot', 'played', 'highest_win_streak', 'elo', 'projectile_kills', 'melee_dealt', 'melee_taken'],
            **kwargs: Missing
        ) -> CombinedLeaderboard | list[dict]:
        """
        Leaderboard API
        ~~~~~~~~~~

        Parameters:
            - gamemode (Literal) :  Minigame name.
            - interval (Literal) : Timespan of the stats.
            - mode (Literal) : mode of the minigames.
            - stats (Literal) : type of leaderboard you want.
        
        Returns:
            - List

        Raise:
            - `APIBlockedException` if request is getting blocked.
            - `APIResponseError` if API isn't responding.
        """
        Check().__leaderboard_input__(gamemode, interval, mode, stats)
        Leaderboard_ = []
        offset = 0
        for _ in range(0, 14):
            Leaderboard_.append(self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, 25, kwargs=kwargs))
            offset += 25

        return CombinedLeaderboard(await packages.asyncio.gather(*[task for task in Leaderboard_])).__Leaderboard__()

    
    async def Status(
            self,
            **kwargs: Missing
        ) -> NetworkStatus | None:
        """
        Network Status API
        ~~~~~~~~~~
        
        Returns:
        - 'PikaNetworkStatus'
        - None if failed to get status
        """
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config
        await RateLimits.avoid_rate_limits()
        async with self.session.get("https://api.craftigames.net/count/play.pika-network.net") as resp:
            if resp.status == 200:
                return NetworkStatus(packages.json.loads(await resp.text()))
            elif Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Status()
            else:
                return None

    
    async def Recap(
            self,
            key: str,
            **kwargs: Missing
        ) -> 'Recap':
        """
        Recap API
        ~~~~~~~~~~

        Parameters:
            - key (str) : recap id.
        
        Returns:
            - Recap (class) if the correct key (recap_id) has been passed.
            - None if the the key (recap_id) is invaild.

        Raise:
            - `APIBlockedException` if request is getting blocked.
            - `APIResponseError` if API isn't responding.
        """
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config
        await RateLimits.avoid_rate_limits()
        async with self.session.get(f"https://stats.pika-network.net/api/recaps/{key}") as resp:

            status = resp.status

            if status == 200:
                return Recap(await resp.json())
            
            elif status == 404 or status == 400 or status == 204:
                packages.asyncio.create_task(log(key, ': recap not found!'))
                return None
            
            elif status == 429 and Recursion <= config.allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Recap(key, Recursion=Recursion)
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass


    async def Punishment(
            self,
            player: str,
            **kwargs: Missing
        ) -> Union[History, None]:
        """
        Punishment
        ~~~~~~~~~

        Parameters:
            - player (str): username of the player.
            
        Returns:
            - History
            - None
        
        Example
        ~~~~~~

        ~~~
        from CraftiGames import Pikanetwork
        import asyncio

        async def Example(player: str):
            
            async with Pikanetwork() as API:
            
                punishment = await API.Punishment(player)

            if punishment is None:
                return
            
            warnings = await punishment.warns()
            
            # and many more...

            print(wins, losses, losses_leaderboard, wlr, final_kills_leaderboard)
        
        asyncio.run(Example(player='AnyPlayer'))
        """
        Recursion = kwargs.get('Recursion', 0)
        RaiseError = kwargs.get('RaiseError', True)
        from .utils import config
        await RateLimits.avoid_rate_limits()
        async with self.session.get(f'https://pika-network.net/bans/search/{player}/') as resp:
            status = resp.status

            if status == 200:
                return History(await resp.text())
            
            elif status == 429 and Recursion <= config.allowed_recursion:

                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(config.delay_after_exceeding_ratelimit)
                return await self.Punishment(player)
            
            elif status == 403 and RaiseError:
                raise APIBlockedException()
            
            else:
                if RaiseError:
                    raise APIResponseError(status_code=status)
                else: pass

    # MultiProcessings
    
    async def MultiProfile(
            self,
            players: List[str],
            ) -> list[tuple[str, 'PikaProfile']]:
        """
        Fetch Multiple Player Profiles
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Processes a list of player usernames and fetches their profiles asynchronously.

        Parameters:
            - players (List[str]) : A list of player usernames to fetch profiles for.

        Returns:
            - Array (List[tuple[str, PikaProfile]]) : A list of tuples, each containing a player's username 
            and their associated profile. If a player is not registered on PikaNetwork, their profile will be `None`.

        :NOTE:
            This function suppresses any errors encountered during profile retrieval, meaning 
            errors will not be raised, but they are not resolved either.

        Example:
            https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/MultiProfile.py
        """
        from .utils import config
        profile = []

        for i in range(0, len(players), config.batch_size):
            batch_members = players[i:i + config.batch_size]
            batch_member_stats = await packages.asyncio.gather(*(self.Profile(member, RaiseError=False) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    profile.append((member, None))
                    continue

                profile.append((member, member_stats))

            await packages.asyncio.sleep(config.batch_delay)

        return profile
    

    async def MultiStats(
            self,
            players: List[str],
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"]
            ) -> List[Tuple[str, Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice, None]]]:
        """
        Fetch Multiple Player Stats
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Retrieves statistics for a list of players across different game modes and intervals asynchronously.

        Parameters:
            - players (List[str]) : A list of player usernames to fetch stats for.
            - gamemode (Literal) : The specific minigame for which stats are retrieved (e.g., bedwars, skywars).
            - interval (Literal) : The timespan for which stats are retrieved (e.g., weekly, monthly).
            - mode (Literal) : The specific mode within the minigame (e.g., solo, doubles).

        Returns:
            - Array (List[Tuple[str, Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice, None]]]) : A list of tuples, each containing a player's username and their associated stats. 
            If a player has their stats hidden from the API or has not registered on Pikanetwork, the stats will be `None`.
        
        :NOTE:
            This function suppresses any errors encountered during stats retrieval, meaning 
            errors will not be raised, but they are not resolved either.
        Example:
            https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/MultiStats.py
        """
        from .utils import config
        stats = []

        for i in range(0, len(players), config.batch_size):
            batch_members = players[i:i + config.batch_size]
            batch_member_stats = await packages.asyncio.gather(*(self.Stats(member, gamemode, interval, mode, RaiseError=False) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    stats.append((member, None))
                    continue

                stats.append((member, member_stats))

            await packages.asyncio.sleep(config.batch_delay)

        return stats
    

    async def MultiGuilds(
            self,
            guilds: List[str],
            ) -> List[Tuple[str, 'Guild']]:
        """
        Fetch Multiple Guilds
        ~~~~~~~~~~~~~~~~~~~~~

        Retrieves data for a list of guilds asynchronously.

        Parameters:
            - guilds (List[str]) : A list of guild names to fetch data for.

        Returns:
            - Array (List[Tuple[str, 'Guild']]) : A list of tuples, each containing a guild's name 
            and its associated `Guild` class. If a guild name is invalid, the corresponding 
            `Guild` class will be `None`.

        :NOTE:
            This function suppresses any errors encountered during Guild retrieval, meaning 
            errors will not be raised, but they are not resolved either.

        Example:
            https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/MultiGuilds.py
        """
        from .utils import config
        guilds_ = []

        for i in range(0, len(guilds), config.batch_size):
            batch_guilds = guilds[i:i + config.batch_size]
            batch_guild_ = await packages.asyncio.gather(*(self.Guild(guild, RaiseError=False) for guild in batch_guilds))
            for guild, guild_api in zip(batch_guilds, batch_guild_):
                if guild_api is None:
                    guilds_.append((guild, None))
                    continue

                guilds_.append((guild, guild_api))

            await packages.asyncio.sleep(config.batch_delay)

        return guilds_
    

    async def MultiRecaps(
            self,
            ids: List[str]
        ) -> List[Tuple[str, 'Recap']]:
        """
        Fetch Multiple Recaps
        ~~~~~~~~~~~~~~~~~~~~~

        Retrieves recap data for a list of IDs/keys asynchronously.

        Parameters:
            - ids (List[str]) : A list of IDs/keys to fetch recap data for.

        Returns:
            - Array (List[Tuple[str, 'Recap']]) : A list of tuples, each containing an ID/key and its 
            associated `Recap` class. If an ID/key is invalid, the corresponding `Recap` class 
            will be `None`.

        :NOTE:
            This function suppresses any errors encountered during Guild retrieval, meaning 
            errors will not be raised, but they are not resolved either.

        Example:
            https://github.com/sti1ltyping/CraftiGames.py-Examples/blob/main/MultiRecaps.py
        """
        from .utils import config
        recaps = []

        for i in range(0, len(ids), config.batch_size):
            batch_keys = ids[i:i + config.batch_size]
            batch_keys_ = await packages.asyncio.gather(*(self.Recap(key, RaiseError=False) for key in batch_keys))
            for recap_id, recap_api in zip(batch_keys, batch_keys_):
                if recap_api is None:
                    recaps.append((recap_id, None))
                    continue

                recaps.append((recap_id, recap_api))

            await packages.asyncio.sleep(config.batch_delay)

        return recaps