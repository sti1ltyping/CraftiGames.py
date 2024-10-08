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

from .RefactorAPI.Guilds import Clan
from .RefactorAPI.Profiles import JartexProfile
from .RefactorAPI.Leaderboard import CombinedLeaderboard
from .RefactorAPI.NetworkStatus import NetworkStatus
from .RefactorAPI.Recaps import Recap

from .Games.Bedwars import Bedwars
from .Games.Skywars import Skywars

from .Punishments import History

from .Ratelimits import (
    JartexNetworkRateLimitHandler as jr_
)

from .ResponseError import faulty

from ._Logger import log

from .utils import config

from .utils import Check

from .utils import (
    APIBlockedException,
    APIResponseError,
    Do_Not_Touch
)

from typing import (
    Union, Literal, List, Tuple
)


allowed_recursion = config.allowed_recursion
batch_size = config.batch_size
batch_delay = config.batch_delay
delay_after_exceeding_ratelimit = config.delay_after_exceeding_ratelimit


class JartexAnnotations:
    """
    Helper class
    ~~~~~~~~
    =============

    - Represents `TypeAnnotation` for JartexNetwork's API wrapper.
    """
    Stats = Union[Bedwars, Skywars]
    Profile = JartexProfile
    Clan  = Clan
    Punishments = History
    Status = NetworkStatus
    Recap = Recap
    Jartexnetwork: 'Jartexnetwork' = None, ...
    JartexAnnotations: 'JartexAnnotations' = None, ...


class Jartexnetwork:
    """
    Jartexnetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~
    A basic wrapper for the JartexNetwork's API.

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
        self.session = packages.aiohttp.ClientSession(headers = await header())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()

    
    class JartexAnnotations:
        """
        Helper class
        ~~~~~~~~
        =============

        - Represents `TypeAnnotation` for JartexNetwork's API wrapper.
        """
        Stats = Union[Bedwars, Skywars]
        Profile = JartexProfile
        Clan  = Clan
        Punishments = History
        Status = NetworkStatus
        Recap = Recap
        Jartexnetwork: 'Jartexnetwork' = None, ...
        JartexAnnotations: 'JartexAnnotations' = None, ...


    async def Profile(
            self,
            player: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[JartexProfile, None]:
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
        from CraftiGames import Jartexnetwork, JartexAnnotations
        import asyncio


        AnyPlayer: str = ...

        async def example():

            async with Jartexnetwork() as api:

                profile = await api.Profile(AnyPlayer)
                
                # Additionally you can also get the skin (BYTES) of the player.
                skin = await profile.skin.Default.face()

            if profile is None:
                return print(AnyPlayer, "has not registered on JartexNetwork.")
            
            username: str = profile.username
            level: int = profile.level
            rank: str = profile.rank
            discord_verified: bool = profile.discord_verified
            
            # and many more...

            if discord_verified:
                print(AnyPlayer, 'has verified their discord account.')

            # Extract the guild from player's profile
            # Returns 'Guild' class if player is in a guild else returns None
            clan = profile.clan()  

            if clan:
                name = clan.name
                leader = clan.owner
                # and many more...

                print(f"{username} is a member of {name}. Leader of that owner is {owner}")

            print(username, level, rank)


        asyncio.run(example())
        """
        await jr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.jartexnetwork.com/api/profile/{player}') as resp:

            status = resp.status

            if status == 200:
                return JartexProfile(await resp.json(), session=self.session)

            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Profile(player)

            elif status == 400 or status == 204 or status == 404:
                packages.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()
   

    async def Stats(
            self,
            player: str,
            gamemode: Literal["bedwars", "skywars"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[Bedwars, Skywars, None]:
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
        from CraftiGames import Jartexnetwork, JartexAnnotations
        import asyncio


        AnyPlayer: str = ...

        async def example():

            async with Jartexnetwork() as api:

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

        await jr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.jartexnetwork.com/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:

            status = resp.status

            if status == 200:
                data: dict = await resp.json()

                if await faulty(data) and Recursion <= allowed_recursion:
                    Recursion += 1
                    packages.asyncio.create_task(log('Faulty Stats detected: ', Recursion, 'X'))
                    return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)

                return {
                    'bedwars': Bedwars,
                    'skywars': Skywars
                }.get(
                    gamemode,
                    lambda x: None
                )(data)


            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)
            
            elif status == 204:
                packages.asyncio.create_task(log(player, ' is hidden from the API!'))
                return None
            
            elif status == 400 or status == 404:
                packages.asyncio.create_task(log(player, ' not found!'))
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def Clan(
            self,
            clan: str,
            *,
            Recursion: 'Do_Not_Touch' = 0
            ) -> Union[Clan, None]:
        """
        Clan API
        ~~~~~~~~~

        Parameters:
            - clan (str): Name of the clan.
            
            Returns:
            - If clan is found returns ClanContext.
            - Returns None if unable to find the clan.
        
        Example
        ~~~~~~

        ~~~
        from CraftiGames import Jartexnetwork, JartexAnnotations
        import asyncio


        AnyClan: str = ...

        async def example():

            async with from Jartexnetwork() as api:

                clan = await api.Clan(AnyClan)
            
            if clan is None:
                return print("clan not found!")
            
            name = clan.name
            tag = clan.tag
            level = clan.level
            member_list = clan.member_list
            member_count = clan.member_count
            owner = clan.owner

            # and more...

            print(name, tag, level, member_count, owner)
            print(member_list)

        asyncio.run(example())
        """
        await jr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.jartexnetwork.com/api/clans/{clan}') as resp:

            status = resp.status

            if status == 200:
                return Clan(await resp.json())
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Clan(clan)
            
            elif status == 400 or status == 204 or status == 404:
                packages.asyncio.create_task(log(clan, ' not found!'))
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

        await jr_.avoid_rate_limits()
        async with self.session.get(f'https://stats.jartexnetwork.com/api/leaderboards?type={gamemode}&stat={stats}&interval={interval}&mode={mode}&offset={offset}&limit={limit}') as resp:
            
            status = resp.status

            if status == 200:
                return await resp.json()
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.__leaderboard__helper__(gamemode, stats, interval, mode, offset, limit, Recursion=Recursion)
            
            elif status == 400 or status == 204 or status == 404:
                return None
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()


    async def Leaderboard(
            self,
            gamemode: Literal["bedwars", "skywars"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"],
            stats: Literal['wins', 'losses', 'kills', 'deaths', 'final_kills', 'final_deaths', 'bed_destroyed', 'melee_kills', 'void_kills', 'bow_kills', 'arrows_hit', 'arrows_shot', 'played', 'highest_win_streak', 'projectile_kills']
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

        return CombinedLeaderboard(await packages.asyncio.gather(*[task for task in Leaderboard_])).__Leaderboard__()

    
    async def Status(
            self,
            *,
            Recursion: 'Do_Not_Touch' = 0
        ) -> NetworkStatus:
        """
        Network Status API
        ~~~~~~~~~~
        
        Returns:
        - 'NetworkStatus'
        """
        await jr_.avoid_rate_limits()
        async with self.session.get("https://api.craftigames.net/count/play.jartexnetwork.com") as resp:
            if resp.status == 200:
                return NetworkStatus(packages.json.loads(await resp.text()))
            elif Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
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
        await jr_.avoid_rate_limits()
        async with self.session.get(f"https://stats.jartexnetwork.com/api/recaps/{key}") as resp:

            status = resp.status

            if status == 200:
                return Recap(await resp.json())
            
            elif status == 404 or status == 400 or status == 204:
                packages.asyncio.create_task(log(key, ': recap not found!'))
                return None
            
            elif status == 429 and Recursion <= allowed_recursion:
                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
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
        from CraftiGames import Jartexnetwork
        import asyncio

        async def Example(player: str):
            
            async with Jartexnetwork() as API:
            
                punishment = await API.Punishment(player)

            if punishment is None:
                return
            
            warnings = await punishment.warns()
            
            # and many more...

            print(wins, losses, losses_leaderboard, wlr, final_kills_leaderboard)
        
        asyncio.run(Example(player='AnyPlayer'))
        """
        await jr_.avoid_rate_limits()
        async with self.session.get(f'https://jartexnetwork.com/bans/search/{player}/') as resp:
            status = resp.status

            if status == 200:
                return History(await resp.text())
            
            elif status == 429 and Recursion <= allowed_recursion:

                Recursion += 1
                packages.asyncio.create_task(log('Exceeded ratelimit: ', Recursion, 'X'))
                await packages.asyncio.sleep(delay_after_exceeding_ratelimit)
                return await self.Punishment(player)
            
            elif status == 403:
                raise APIBlockedException()
            
            else:
                raise APIResponseError()

    # MultiProcessings

    async def MultiProfile(
            self,
            api: 'Jartexnetwork',
            players: list[str],
            ) -> list[tuple[str, 'JartexProfile']]:
        """
        Multiple Profiles
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Jartexnetork class
            - players: List of players.
            
        Returns:
            - An array of players usernames and profile, it can further be used to extract specific items from profile.
            - Profile is None for any players that are not registered on Jartexnetork.
        
        Example
        ~~~~~~

        ~~~
        from CraftiGames import Jartexnetwork, JartexAnnotations
        import asyncio


        List_of_Players: list = [...]

        async def example():

            async with Jartexnetork() as api:
                response = await api.MultiProfile(api, List_of_Players)
            
            for username, profile_api in response:
                profile_api: JartexAnnotations.Profile    # Annotations for profile api

                # Error handling
                if profile_api is None:
                    print(f"Couldn't find {username}")      # Player has not registered on Jartexnetork.
                    continue

                print(username, profile_api.rank)
                

        asyncio.run(example())
        """
        profile = []

        for i in range(0, len(players), batch_size):
            batch_members = players[i:i + batch_size]
            batch_member_stats = await packages.asyncio.gather(*(api.Profile(member) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    profile.append((member, None))
                    continue

                profile.append((member, member_stats))

            await packages.asyncio.sleep(batch_delay)

        return profile
    

    async def MultiStats(
            self,
            api: 'Jartexnetwork',
            players: list[str],
            gamemode: Literal["bedwars", "skywars"],
            interval: Literal["weekly", "monthly", "yearly", "total"],
            mode: Literal["all_modes", "solo", "doubles", "triples", "quad"]
            ) -> list[tuple[str, Union[Bedwars, Skywars]]]:
        """
        Multiple stats
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Jartexnetork class
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
        from CraftiGames import Jartexnetork, JartexAnnotations
        import asyncio


        List_of_Players: list = [...]

        async def example():

            async with Jartexnetork() as api:
                response = await api.Stats(api, List_of_Players, "total", "all_modes")
            
            for username, stats_api in response:
                stats_api: JartexAnnotations.Stats    # Annotations for stats api

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
            batch_member_stats = await packages.asyncio.gather(*(api.Stats(member, gamemode, interval, mode) for member in batch_members))
            for member, member_stats in zip(batch_members, batch_member_stats):
                if member_stats is None:
                    stats.append((member, None))
                    continue

                stats.append((member, member_stats))

            await packages.asyncio.sleep(batch_delay)

        return stats
    

    async def MultiClans(
            self,
            api: 'Jartexnetwork',
            guilds: list[str],
            ) -> list[tuple[str, 'Clan']]:
        """
        Multiple Clans
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Jartexnetork class.
            - clans: List of clans.
            
        Returns:
            - An array of clan's names and clan class, it can further be used to extract specific items from the clan class.
            - Clan is None for any invalid clan.
        
        Example
        ~~~~~~

        ~~~
        from CraftiGames import Jartexnetork, JartexAnnotations
        import asyncio


        List_of_Clans: list = [...]

        async def example():

            async with Pikanetwork() as api:
                response = await api.MultiClans(api, List_of_Clans)
            
            for name, clan_api in response:
                clan_api: JartexAnnotations.Clan    # Annotations for clan api

                # Error handling
                if clan_api is None:
                    print(f"Couldn't find {name}")      # Incorrect clan name
                    continue

                print(name, clan_api.level)
                

        asyncio.run(example())
        """
        guilds_ = []

        for i in range(0, len(guilds), batch_size):
            batch_guilds = guilds[i:i + batch_size]
            batch_guild_ = await packages.asyncio.gather(*(api.Guild(guild) for guild in batch_guilds))
            for guild, guild_api in zip(batch_guilds, batch_guild_):
                if guild_api is None:
                    guilds_.append((guild, None))
                    continue

                guilds_.append((guild, guild_api))

            await packages.asyncio.sleep(batch_delay)

        return guilds_
    

    async def MultiRecaps(
            self,
            api: 'Jartexnetwork',
            ids: List[str]
        ) -> List[Tuple[str, 'Recap']]:
        """
        Multiple Recaps
        ~~~~~~~~~~~~~~

        Parameters:
            - api: Instance of Jartexnetork class
            - ids: List of ids/keys.
            
        Returns:
            - An array of id and Recap class, it can further be used to extract specific items from the Recap class.
            - Recap is None for any invalid id/key.
        
        Example
        ~~~~~~

        ~~~
        from CraftiGames import Jartexnetork, JartexnAnnotations
        import asyncio


        Ids_of_recaps: list = [...]

        async def example():

            async with Jartexnetork() as api:
                response = await api.MultiRecaps(api, Ids_of_recaps)
            
            for id, recap_api in response:
                recap_api: JartexAnnotations.Recap    # Annotations for recap api

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
            batch_keys_ = await packages.asyncio.gather(*(api.Recap(key) for key in batch_keys))
            for recap_id, recap_api in zip(batch_keys, batch_keys_):
                if recap_api is None:
                    recaps.append((recap_id, None))
                    continue

                recaps.append((recap_id, recap_api))

            await packages.asyncio.sleep(batch_delay)

        return recaps