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
from .utils import get_driver

from .RefactorAPI.Guilds import Guild
from .RefactorAPI.Profiles import Profile
from .RefactorAPI.Leaderboard import Sort

from .Games.Bedwars import Bedwars
from .Games.Skywars import Skywars
from .Games.Practice import Unrankedpractice, Rankedpractice

from .Punishments import History

from .Ratelimits import avoid_rate_limits

from .ResponseError import faulty

from .__Logger__ import log

from .utils import (
    Allowed_Recursion,
    batch_size,
    batch_delay,
    delay_after_exceeding_ratelimit
)

from .utils import Check

from typing import (
    Union, Literal, List
)


class PikaAnnotations:
    """
    Helper class
    ~~~~~~~~
    =============

    - Represents `TypeAnnotation` for this API wrapper.
    """
    Stats = Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]
    Profile = Profile
    Guild = Guild
    Punishments = History


class Pikanetwork:
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~
    A basic wrapper for the PikaNetwork's API.

    =============================

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

        - Represents `TypeAnnotation` for this API wrapper.
        """
        Stats = Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]
        Profile = Profile
        Guild = Guild
        Punishments = History


    async def Profile(
            self,
            player: str,
            *,
            Recursion = 0
            ) -> Union[Profile, None]:
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
            minigame_rank = await player.highest_minigame_rank()
            practice_rank = await player.highest_practice_rank()
            
            guild = await player.guild()
            if guild is None:
                return 'Player is not in a guild'
            
            guild_name = await guild.name()
            
            # and many more...

            print(usename, level, minigame_rank, practice_rank, guild_name)
        
        asyncio.run(Example(playerING='AnyPlayer'))
        """
        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:

            status = resp.status

            if status == 200:
                return Profile(await resp.json(), session=self.session)

            elif status == 429 and Recursion <= Allowed_Recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Profile(player)

            elif status == 400 or status == 204:
                return None
            
            else:
                imports.asyncio.create_task(log(status, ' error!'))
                return None
   

    async def Stats(
            self,
            player: str,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            *,
            Recursion = 0
            ) -> Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice, None]:
        """
        Stats API
        ~~~~~~~~~

        Parameters:
            - player (str): Ingame name of the player.
            - gamemode (Union): minigame of the stats.
            - interval (Union): Timespan of the stats.
            - mode (Union): mode of the minigames.
            
            Returns:
            - If player is found returns minigame.
            - Returns None if unable to find player.

            Raise:
            - Error if gamemode, interval or mode is invalid.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(playerING: str):
            
            async with Pikanetwork() as API:
            
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
        player = str(player)
        gamemode: str = gamemode.lower()
        interval: str = interval.lower()
        mode: str = mode.upper()

        Check().__stats_input__(gamemode, interval, mode)

        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:

            status = resp.status

            if status == 429 and Recursion <= Allowed_Recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)
            
            elif status == 204:
                imports.asyncio.create_task(log(player, ' is hidden from the API!'))
                return None

            elif status == 400:
                return None

            data = await resp.json()

            if await faulty(data) and Recursion <= Allowed_Recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Faulty Stats detected: ', Recursion))
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)

            if gamemode == 'bedwars':
                return Bedwars(data)
            elif gamemode == 'skywars':
                return Skywars(data)
            elif gamemode == 'unrankedpractice':
                return Unrankedpractice(data)
            elif gamemode == 'rankedpractice':
                return Rankedpractice(data)


    async def Guild(
            self,
            guild: str,
            *,
            Recursion = 0
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

        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/clans/{guild}') as resp:

            status = resp.status

            if status == 200:
                return Guild(await resp.json())
            
            elif status == 429 and Recursion <= Allowed_Recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Guild(guild)
            
            elif status == 400 or status == 204:
                return None
            
            else:
                imports.asyncio.create_task(log(status, ' error!'))
                return None


    async def __leaderboard__helper__(
            self,
            gamemode,
            stats,
            interval,
            mode,
            offset: int,
            limit: int,
            *,
            Recursion = 0
        ) -> Union[dict, None]:

        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/leaderboards?type={gamemode}&stat={stats}&interval={interval}&mode={mode}&offset={offset}&limit={limit}') as resp:
            status = resp.status
            if status == 200:
                return await resp.json()
            elif status == 429 and Recursion <= Allowed_Recursion:
                Recursion += 1
                imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, limit, Recursion=Recursion)
            elif status == 400 or status == 204:
                return None
            else:
                imports.asyncio.create_task(log(status, ' error!'))
                return None

    async def Leaderboard(
            self,
            gamemode: Literal["bedwars", "skywars", "unrankedpractice", "rankedpractice"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            stats: Literal['wins', 'losses', 'kills', 'deaths', 'final_kills', 'final_deaths', 'bed_destroyed', 'melee_kills', 'void_kills', 'bow_kills', 'arrows_hit', 'arrows_shot', 'played', 'highest_win_streak', 'elo''projectile_kills', 'melee_dealt', 'melee_taken']
        ) -> list[dict]:
        
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
        for k in range(0, 14):
            Leaderboard_.append(self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, 25))
            offset += 25

        return Sort(await imports.asyncio.gather(*[task for task in Leaderboard_])).__Leaderboard__()


    async def Punishment(
            self,
            player: str,
            *,
            Recursion = 0
        ) -> Union[History, None]:

        """
        Punishment
        ~~~~~~~~~

        Parameters:
            - player (str): Ingame name of the player.
            
            Returns:
            - If player is found returns minigame.
            - Returns None if unable to find player.

            Raise:
            - Error if gamemode, interval or mode is invalid.
        
        Example
        ~~~~~~

        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(player: str):
            
            async with Pikanetwork() as API:
            
                punishment = await API.Punishment(player)

                if punishment is None:
                    return '404'
                
                warnings = await punishment.warns()
                
                # and many more...

                print(wins, losses, losses_leaderboard, wlr, final_kills_leaderboard)
        
        asyncio.run(Example(player='AnyPlayer'))
        """
        await avoid_rate_limits()
        async with self.session.get(f'https://pika-network.net/bans/search/{player}/') as resp:
            status = resp.status

            if status == 200:
                return History(await resp.text())
            elif Recursion <= Allowed_Recursion:
                Recursion += 1
                await imports.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await imports.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Punishment(player)
            else:
                return None

    # MultiProcessings
    
    async def MultiProfile(
            self,
            api: 'Pikanetwork',
            players: List[str],
            ) -> list['Profile']:
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
        import PikaPY
        from PikaPY import Pikanetwork

        import asyncio


        async def main(Player: str) -> None:
            
            async with Pikanetwork as api:
                
                player = await api.Profile(Player)
                if player is None:
                    return print(Player, 'is not registered on PikaNetwork.')
                
                friends = await player.friend_list()
                if friends is None:
                    return print(Player, 'has no friends'.)

                member_stats = await api.MultiProfile(api, friends)

                for member, stats in member_stats:
                    profile: PikaPY.Games.Bedwars.Bedwars

                    level = await profile.level()
                    rank = await profile.highest_minigame_rank()
                    print(member, level, rank)

                    
        asyncio.run(main('AnyPlayer'))
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
            ) -> Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice]:
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
            - An array of players usernames and stats (Games class), it can further be used to extract specific stats.
            - stats (Games class) is None for the players hidden from the API.
        
        Example
        ~~~~~~

        ~~~
        import PikaPY
        from PikaPY import Pikanetwork

        import asyncio


        async def main(Player: str) -> None:
            
            async with Pikanetwork as api:
                
                player = await api.Profile(Player)
                if player is None:
                    return print(Player, 'is not registered on PikaNetwork.')
                
                guild = await player.guild()
                if guild is None:
                    return print(Player, 'is not in a guild'.)

                members = await guild.member_list()

                member_stats = await api.MultiStats(api, members, 'bedwars', 'total', 'all_modes')

                for member, stats in member_stats:
                    stats: PikaPY.Games.Bedwars.Bedwars

                    if stats is None:
                        print(member, 'is hidden from the API.')
                        continue
                    wins = await stats.wins(leaderboard=False)
                    print(member, wins)

                    
        asyncio.run(main('AnyPlayer'))
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
            ) -> 'Guild':
        """
        Multiple Guilds
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Pikanetwork class
            - guilds: List of guilds.
            
        Returns:
            - An array of guild's usernames and guild class, it can further be used to extract specific items from the guild class.
            - Guild is None for any invalid guild.
        
        Example
        ~~~~~~

        ~~~
        import PikaPY
        from PikaPY import Pikanetwork

        import asyncio


        async def main() -> None:
            
            async with Pikanetwork as api:
                
                # These are just for example they may not exists for real!
                guilds = ['Winds', 'Champs', 'Apples', 'PikaUwU'] 

                guilds_infos = await MultiGuilds(api, guilds)

                for guild, guild_api in guilds_infos:
                    
                    if guild_api is None:
                        continue # skips the invalid guild.
                        
                    owner = await guild_api.leader()
                    level = await guild_api.level()

                    print(guild, owner, level)

                    
        asyncio.run(main())
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