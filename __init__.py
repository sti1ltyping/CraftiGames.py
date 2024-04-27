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

from typing import Union

# Global batch size
batch_size = 15


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
            mode: Union[all_modes, solo, doubles, triples, quad]
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
            
            API = Pikanetwork()
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

        await avoid_rate_limits()
        async with self.session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:
            if resp.status != 200:
                try:
                    if gamemode not in Gamemodes():
                        raise ValueError('Invalid gamemode has been passed')
                    elif interval not in Intervals():
                        raise ValueError('Invalid interval has been passed')
                    elif mode not in Modes():
                        raise ValueError('Invalid mode has been passed')
                    else:
                        return None
                except Exception as e:
                    print(e)
                    return None 
            
            data = await resp.json()

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
    
    async def ProfileBatch(
            self,
            players: list[str]
            ) -> list:
        """
        Fetches profiles for multiple players in batches of 15.

        Parameters:
            - players (list[str]): List of player names to fetch profiles for.

        Returns:
            - A list of profiles for all players.

        Example:
        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(players: list[str]):
            API = Pikanetwork()
            profiles = await API.ProfileBatch(players)
            for profile in profiles:
                if profile is not None:
                    print(profile)  # Process the profile here

        asyncio.run(Example(players=['Player1', 'Player2', 'Player3']))
        """

        profiles = []

        for i in range(0, len(players), batch_size):
            current_batch = players[i:i + batch_size]
            batch_profiles = await self._fetch_batch_profiles(current_batch)
            profiles.extend(batch_profiles)

        return profiles

    async def GuildBatch(
            self,
            guilds: list[str]
            ) -> list:
        """
        Fetches guilds for multiple guild names in batches.

        Parameters:
            - guilds (list[str]): List of guild names to fetch.

        Returns:
            - A list of guilds for all guild names.

        Example:
        ~~~
        from PikaPY import Pikanetwork
        import asyncio

        async def Example(guilds: list[str]):
            API = Pikanetwork()
            guilds_data = await API.GuildBatch(guilds)
            for guild_data in guilds_data:
                if guild_data is not None:
                    print(guild_data)  # Process the guild data here

        asyncio.run(Example(guilds=['Guild1', 'Guild2', 'Guild3']))
        """

        guilds_data = []

        for i in range(0, len(guilds), batch_size):
            current_batch = guilds[i:i + batch_size]
            batch_guilds = await self._fetch_batch_guilds(current_batch)
            guilds_data.extend(batch_guilds)

        return guilds_data

    async def _fetch_batch_profiles(
            self,
            players: list[str]
            ) -> list:
        """
        Helper function to fetch profiles for a batch of players.

        Parameters:
            - players (list[str]): List of player names to fetch profiles for.

        Returns:
            - A list of profiles for the players in the batch.
        """
        batch_profiles = []

        async with self.session:
            for player in players:
                profile = await self.Profile(player)
                batch_profiles.append(profile)
                await asyncio.sleep(1)  # Add a delay to avoid rate limiting

        return batch_profiles

    async def _fetch_batch_guilds(
            self,
            guilds: list[str]
            ) -> list:
        """
        Helper function to fetch guilds for a batch of guild names.

        Parameters:
            - guilds (list[str]): List of guild names to fetch.

        Returns:
            - A list of guilds for the guild names in the batch.
        """
        batch_guilds = []

        async with self.session:
            for guild_name in guilds:
                guild = await self.Guild(guild_name)
                batch_guilds.append(guild)
                await asyncio.sleep(1)  # Add a delay to avoid rate limiting

        return batch_guilds