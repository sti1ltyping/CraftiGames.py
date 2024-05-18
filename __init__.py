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
    Weekly as weekly,
    Monthly as monthly,
    Yearly as yearly,
    Total as total,
    
    All_Modes as all_modes,
    Solo as solo,
    Doubles as doubles,
    Triples as triples,
    Quadriples as quad
)

from .utils import *

from .guilds import GUILD
from .PlayerProfile import Profile

from .Games.Bedwars import Bedwars
from .Games.Skywars import Skywars
from .Games.Practice import Unrankedpractice, Rankedpractice

from .Ratelimits import avoid_rate_limits

from .ResponseError import faulty

from ._Logs import log

from typing import Union, Literal, Coroutine


batch_size = 15
Allowed_Recursion = 100

class Pikanetwork:
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~
    A basic wrapper for the PikaNetwork's API.
    """

    def __init__(self):
        self.session = None
        self.cache = {}

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()


    async def Profile(
            self,
            player: str
            ) -> (Profile | None):
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

            if int(resp.status) !=  200:
                return None
            data = await resp.json()

            return Profile(data)
            

    async def Stats(
            self,
            player: str,
            gamemode: Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice],
            interval: Union[weekly, monthly, yearly, total],
            mode: Union[all_modes, solo, doubles, triples, quad],
            *,
            Recursion = 0
            ) -> (Bedwars | Skywars | Unrankedpractice | Rankedpractice | None):
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

        player: str = player
        gamemode: str = gamemode.lower()
        interval: str = interval.lower()
        mode: str = mode.upper()

        #await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:
            await log(resp.status)
            status = resp.status
            # 💢 Ratelimit
            if status == 429 and Recursion <= Allowed_Recursion:
                Recursion += 1
                await log('Ratelimit, trying to fix the stats', Recursion=Recursion)
                await asyncio.sleep(1.5)
                return await self.Stats(player, gamemode, interval, mode, Recursion=Recursion)
            # 👻 Hidden from API
            elif status == 204:
                await log('is hidden from the API!', player)
                return None # Hidden from API
            # ⚠️ Invalid format | Player does not exists ⚠️
            elif status == 400:
                try:
                    if gamemode not in Gamemodes.all():
                        raise ValueError('⚠️ Invalid gamemode has been passed!')
                    elif interval not in Intervals.all():
                        raise ValueError('⚠️ Invalid interval has been passed!')
                    elif mode not in Modes.all():
                        raise ValueError('⚠️ Invalid mode has been passed!')
                    else:
                        await log('does not exists!', player)
                        return None
                except Exception as error:
                    await log(f'An error occure while finding stats of {player}:\n\n' + ''.join(traceback.format_exception(type(error), error, error.__traceback__)))
                    return None 
            # ✔
            data = await resp.json()

            if await faulty(data) and Recursion <= Allowed_Recursion:
                # Retry
                Recursion += 1
                await log(f'⚠️Faulty Stats', Recursion=Recursion)
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
            guild: str
            ) -> (GUILD | None):
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
            if int(resp.status) !=  200:
                return None
            
            data = await resp.json()
            return GUILD(data)

    async def Leaderboard(
            self,
            gamemode: Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice],
            stats: str,
            interval: Union[weekly, monthly, yearly, total],
            mode: Union[all_modes, solo, doubles, triples, quad],

            offset: int,
            limit: int   
    ):
        
        """
        
        """
        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/leaderboards?type={gamemode}&stat={stats}&interval={interval}&mode={mode}&offset={offset}&limit={limit}') as resp:
            if int(resp.status) != 200:
                return None
            
            data = await resp.json()

    # Batch processing 

    async def StatsBatch(
            self,
            players: list[str],
            gamemode: Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice],
            interval: Union[weekly, monthly, yearly, total],
            mode: Union[all_modes, solo, doubles, triples, quad]
            ) -> list:
        """
        Fetches stats for multiple players in batches of 15.

        Parameters:
            - players (list[str]): List of player names to fetch stats for.
            - gamemode (Union): Minigame of the stats.
            - interval (Union): Timespan of the stats.
            - mode (Union): Mode of the minigames.

        Returns:
            - A list of stats for all players.

        Example:
        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(players: list[str]):
            API = Pikanetwork()
            stats = await API.StatsBatch(players, 'bedwars', 'weekly', 'all_modes')
            for player_stats in stats:
                if player_stats is not None:
                    print(player_stats)  # Process the stats here

        asyncio.run(Example(players=['Player1', 'Player2', 'Player3']))
        """
        batch_size = 15
        stats = []

        for i in range(0, len(players), batch_size):
            current_batch = players[i:i + batch_size]
            batch_stats = await self._fetch_batch_stats(current_batch, gamemode, interval, mode)
            stats.extend(batch_stats)

        return stats

    async def _fetch_batch_stats(
            self,
            players: list[str],
            gamemode: Union[Bedwars, Skywars, Unrankedpractice, Rankedpractice],
            interval: Union[weekly, monthly, yearly, total],
            mode: Union[all_modes, solo, doubles, triples, quad]
            ) -> list:
        """
        Helper function to fetch stats for a batch of players.

        Parameters:
            - players (list[str]): List of player names to fetch stats for.
            - gamemode (Union): Minigame of the stats.
            - interval (Union): Timespan of the stats.
            - mode (Union): Mode of the minigames.

        Returns:
            - A list of stats for the players in the batch.
        """
        batch_stats = []

        async with self.session:
            for player in players:
                stats = await self.Stats(player, gamemode, interval, mode)
                batch_stats.append(stats)
                await asyncio.sleep(1)

        return batch_stats