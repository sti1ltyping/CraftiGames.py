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


class Pikanetwork():
    """
    Pikanetwork API Wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~


    A basic wrapper for the PikaNetwork's API.
    """

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
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{player}') as resp:
                if int(resp.status) !=  200:
                    return None
                data = json.loads(await resp.text())

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
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/profile/{player}/leaderboard?type={gamemode}&interval={interval}&mode={mode}') as resp:
                if resp.status != 200:
                    # Raise val error if incorrect filler has been passed!
                    # Removed because bugged!
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
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://stats.pika-network.net/api/clans/{guild}') as resp:
                if int(resp.status) !=  200:
                    return None
                
                data = json.loads(await resp.text())
                return GUILD(data)
