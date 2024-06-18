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

from .utils import imports

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

from .Ratelimits import _pikanetwork as pr_

from .ResponseError import faulty

from ._Logger import log

from .utils import (
    allowed_recursion,
    batch_size,
    batch_delay,
    delay_after_exceeding_ratelimit
)

from .utils import Check

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
    Stats = Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]
    Profile = PikaProfile
    Guild  = Guild
    Punishments = History
    Status = NetworkStatus
    Recap = Recap
    Pikanetwork: 'Pikanetwork' = None, ...
    PikaAnnotations: 'PikaAnnotations' = None, ...


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

    def __init__(self) -> None:
        self.session = None
        self.cache = {...}

    async def __aenter__(self):
        self.session = imports.aiohttp.ClientSession(headers = await header())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()

    
    class PikaAnnotations:
        """
        Helper class
        ~~~~~~~~
        =============

        - Represents `TypeAnnotation` for PikaNetwork's API wrapper.
        """
        Stats = Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]
        Profile = PikaProfile
        Guild  = Guild
        Punishments = History
        Status = NetworkStatus
        Recap = Recap
        Pikanetwork: 'Pikanetwork' = None, ...
        PikaAnnotations: 'PikaAnnotations' = None, ...


    async def Profile(
            self,
            player: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[PikaProfile, None]:
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
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        AnyPlayer: str = ...

        async def example():

            async with Pikanetwork() as api:

                profile = await api.Profile(AnyPlayer)
                
                # Additionally you can also get the skin (BYTES) of the player.
                skin = await profile.skin.Default.face()

            if profile is None:
                return print(AnyPlayer, "has not registered on PikaNetwork.")
            
            username: str = profile.username
            level: int = profile.level
            minigame_rank: str = profile.highest_minigame_rank
            practice_rank: str = profile.highest_practice_rank
            discord_verified: bool = profile.discord_verified
            
            # and many more...

            if discord_verified:
                print(AnyPlayer, 'has verified their discord account.')

            # Extract the guild from player's profile
            # Returns 'Guild' class if player is in a guild else returns None
            guild = profile.guild()  

            if guild:
                name = guild.name
                leader = guild.leader
                # and many more...

                print(f"{username} is a member of {name}. Leader of that guild is {leader}")

            print(username, level, minigame_rank, practice_rank)


        asyncio.run(example())
        """
        await pr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:

            status = resp.status

            if status == 200:
                return PikaProfile(await resp.json(), session=self.session)

            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Profile(player)

            elif status == 400 or status == 204:
                imports.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()
   

    async def Stats(
            self,
            player: str,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice, None]:
        """
        Stats API
        ~~~~~~~~~

        Parameters:
            - player (str): Ingame name of the player.
            - gamemode (Literal): minigame of the stats.
            - interval (Literal): Timespan of the stats.
            - mode (Literal): mode of the minigames.
            
        Returns:
            - If player is found returns minigame.
            - Returns None if unable to find player.

        Raise:
            - Error if gamemode, interval or mode is invalid.
            - `APIBlockedException` if request is getting blocked.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        AnyPlayer: str = ...

        async def example():

            async with Pikanetwork() as api:

                stats = await api.Stats(AnyPlayer, "bedwars", "total", "all_modes")
            
            if stats is None:
                return print("Player not found or Player is hidden from the API!")
            
            wins = stats.wins
            losses = stats.losses
            wlr = stats.wlr
            win_rate = stats.win_rate
            beds_destroyed = stats.beds_destroyed

            # and more...

            print(wins, losses, wlr, win_rate, beds_destroyed)

        asyncio.run(example())
        """
        if Recursion <= 0:
            player, gamemode, interval, mode = str(player), gamemode.lower(), interval.lower(), mode.upper()
            Check().__stats_input__(gamemode, interval, mode)

        await pr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:

            status = resp.status

            if status == 200:
                data: dict = await resp.json()

                if await faulty(data) and Recursion <= allowed_recursion:
                    Recursion += 1
                    imports.asyncio.create_task(log('Faulty Stats detected: ', Recursion, 'X'))
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


            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)
            
            elif status == 204:
                imports.asyncio.create_task(log(player, ' is hidden from the API!'))
                return None
            
            elif status == 400:
                imports.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def Guild(
            self,
            guild: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[Guild, None]:
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
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        AnyGuild: str = ...

        async def example():

            async with Pikanetwork() as api:

                guild = await api.Guild(AnyGuild)
            
            if guild is None:
                return print("Guild not found!")
            
            name = guild.name
            tag = guild.tag
            level = guild.level
            member_list = guild.member_list
            member_count = guild.member_count
            leader = guild.leader

            # and more...

            print(name, tag, level, member_count, leader)
            print(member_list)

        asyncio.run(example())
        """
        await pr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/clans/{guild}') as resp:

            status = resp.status

            if status == 200:
                return Guild(await resp.json())
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Guild(guild)
            
            elif status == 400 or status == 204:
                imports.asyncio.create_task(log(guild, ' not found!'))
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def __leaderboard__helper__(
            self,
            gamemode,
            stats,
            interval,
            mode,
            offset: int,
            limit: int,
            *,
            Recursion: 'Do_Not_Touch' = 0
        ) -> Union[dict, None]:

        await pr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/leaderboards?type={gamemode}&stat={stats}&interval={interval}&mode={mode}&offset={offset}&limit={limit}') as resp:
            
            status = resp.status

            if status == 200:
                return await resp.json()
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, limit, Recursion=Recursion)
            
            elif status == 400 or status == 204:
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def Leaderboard(
            self,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            stats: Literal['wins', 'losses', 'kills', 'deaths', 'final_kills', 'final_deaths', 'bed_destroyed', 'melee_kills', 'void_kills', 'bow_kills', 'arrows_hit', 'arrows_shot', 'played', 'highest_win_streak', 'elo', 'projectile_kills', 'melee_dealt', 'melee_taken']
        ) -> CombinedLeaderboard | list[dict]:
        """
        Leaderboard API
        ~~~~~~~~~~

        Parameters:
        - gamemode: minigame of the stats.
        - interval: Timespan of the stats.
        - mode: mode of the minigames.
        - stats: type of leaderboard you want.
        
        Returns:
        - List
        
        """
        Check().__leaderboard_input__(gamemode, interval, mode, stats)
        Leaderboard_ = []
        offset = 0
        for _ in range(0, 14):
            Leaderboard_.append(self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, 25))
            offset += 25

        return CombinedLeaderboard(await imports.asyncio.gather(*[task for task in Leaderboard_])).__Leaderboard__()

    
    async def Status(
            self,
            *,
            Recursion: 'Do_Not_Touch' = 0
        ) -> NetworkStatus:
        """
        Network Status API
        ~~~~~~~~~~
        
        Returns:
        - 'PikaNetworkStatus'
        """
        await pr_.avoid_rate_limits()
        async with self.session.get("https://api.craftigames.net/count/play.pika-network.net") as resp:
            if resp.status == 200:
                return NetworkStatus(imports.json.loads(await resp.text()))
            elif Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Status()
            else:
                return None

    
    async def Recap(
            self,
            key: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
        ) -> 'Recap':
        """
        Recap API
        ~~~~~~~~~~

        Parameters:
        - key (str): recap id.
        
        Returns:
        - Recap (class) if the correct key (recap_id) has been passed.
        - None if the the key (recap_id) is invaild.
        """
        await pr_.avoid_rate_limits()
        async with self.session.get(f"https://stats.pika-network.net/api/recaps/{key}") as resp:

            status = resp.status

            if status == 200:
                return Recap(await resp.json())
            
            elif status == 404 or status == 400 or status == 204:
                return None
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Recap(key, Recursion=Recursion)
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def Punishment(
            self,
            player: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
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
        from PikaPY import Pikanetwork
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
        await pr_.avoid_rate_limits()
        async with self.session.get(f'https://pika-network.net/bans/search/{player}/') as resp:
            status = resp.status

            if status == 200:
                return History(await resp.text())
            
            elif status == 429 and Recursion <= allowed_recursion:

                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Punishment(player)
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()

    # MultiProcessings
    
    async def MultiProfile(
            self,
            api: 'Pikanetwork',
            players: List[str],
            ) -> list[tuple[str, 'Profile']]:
        """
        Multiple Profiles
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Pikanetwork class
            - players: List of players.
            
        Returns:
            - An array of players usernames and profile, it can further be used to extract specific items from profile.
            - Profile is None for any players that are not registered on PikaNetwork.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        List_of_Players: list = [...]

        async def example():

            async with Pikanetwork() as api:
                response = await api.MultiProfile(api, List_of_Players)
            
            for username, profile_api in response:
                profile_api: PikaAnnotations.Profile    # Annotations for profile api

                # Error handling
                if profile_api is None:
                    print(f"Couldn't find {username}")      # Player has not registered on pikanetwork.
                    continue

                print(username, profile_api.highest_minigame_rank)
                

        asyncio.run(example())
        """
        profile = []

        for i in range(0, len(players), batch_size):
            batch_members = players[i:i + batch_size]
            batch_member_stats = await imports.asyncio.gather(*(api.Profile(member) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    profile.append((member, None))
                    continue

                profile.append((member, member_stats))

            await imports.asyncio.sleep(batch_delay)

        return profile
    

    async def MultiStats(
            self,
            api: 'Pikanetwork',
            players: List[str],
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"]
            ) -> List[Tuple[str, Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]]]:
        """
        Multiple stats
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Pikanetwork class
            - players: List of players.
            - gamemode: Minigame of the stats.
            - interval: Timespan of the stats.
            - mode: Mode of the minigames.
            
        Returns:
            - An array of player's usernames and stats (Games class), it can further be used to extract specific stats.
            - stats (Games class) is None for the players hidden from the API.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        List_of_Players: list = [...]

        async def example():

            async with Pikanetwork() as api:
                response = await api.Stats(api, List_of_Players, "total", "all_modes")
            
            for username, stats_api in response:
                stats_api: PikaAnnotations.Stats    # Annotations for stats api

                # Error handling
                if stats_api is None:
                    print(f"Couldn't find {username}")      # Maybe hidden from the api or incorrect username
                    continue

                print(username, stats_api.wins)
                

        asyncio.run(example())
        """
        stats = []

        for i in range(0, len(players), batch_size):
            batch_members = players[i:i + batch_size]
            batch_member_stats = await imports.asyncio.gather(*(api.Stats(member, gamemode, interval, mode) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    stats.append((member, None))
                    continue

                stats.append((member, member_stats))

            await imports.asyncio.sleep(batch_delay)

        return stats
    

    async def MultiGuilds(
            self,
            api: 'Pikanetwork',
            guilds: List[str],
            ) -> List[Tuple[str, 'Guild']]:
        """
        Multiple Guilds
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Pikanetwork class
            - guilds: List of guilds.
            
        Returns:
            - An array of guild's names and guild class, it can further be used to extract specific items from the guild class.
            - Guild is None for any invalid guild.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        List_of_Guilds: list = [...]

        async def example():

            async with Pikanetwork() as api:
                response = await api.MultiGuilds(api, List_of_Guilds)
            
            for name, guild_api in response:
                guild_api: PikaAnnotations.Guild    # Annotations for stats api

                # Error handling
                if guild_api is None:
                    print(f"Couldn't find {name}")      # Incorrect guild name
                    continue

                print(name, guild_api.level)
                

        asyncio.run(example())
        """
        guilds_ = []

        for i in range(0, len(guilds), batch_size):
            batch_guilds = guilds[i:i + batch_size]
            batch_guild_ = await imports.asyncio.gather(*(api.Guild(guild) for guild in batch_guilds))
            for guild, guild_api in zip(batch_guilds, batch_guild_):
                if guild_api is None:
                    guilds_.append((guild, None))
                    continue

                guilds_.append((guild, guild_api))

            await imports.asyncio.sleep(batch_delay)

        return guilds_
    

    async def MultiRecaps(
            self,
            api: 'Pikanetwork',
            ids: List[str]
        ) -> List[Tuple[str, 'Recap']]:
        """
        Multiple Guilds
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Pikanetwork class
            - ids: List of ids/keys.
            
        Returns:
            - An array of id and Recap class, it can further be used to extract specific items from the Recap class.
            - Recap is None for any invalid id/key.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork, PikaAnnotations
        import asyncio


        Ids_of_recaps: list = [...]

        async def example():

            async with Pikanetwork() as api:
                response = await api.MultiRecaps(api, Ids_of_recaps)
            
            for id, recap_api in response:
                recap_api: PikaAnnotations.Recap    # Annotations for recap api

                # Error handling
                if recap_api is None:
                    print(f"Couldn't find any recap of id: {id}")      # Incorrect id/key
                    continue

                print(id, recap_api.winners)
                

        asyncio.run(example())
        """
        recaps = []

        for i in range(0, len(ids), batch_size):
            batch_keys = ids[i:i + batch_size]
            batch_keys_ = await imports.asyncio.gather(*(api.Recap(key) for key in batch_keys))
            for recap_id, recap_api in zip(batch_keys, batch_keys_):
                if recap_api is None:
                    recaps.append((recap_id, None))
                    continue

                recaps.append((recap_id, recap_api))

            await imports.asyncio.sleep(batch_delay)

        return recaps