PikaPY
==========

Pikanetwork API Wrapper
A easy to use, feature-rich, and Asynchronous warpping.

Key Features
-------------

- Wraps Pikanetwork's API Asynchronously.
- Fast and efficient.
- Handles Ratelimits, ResponseErrors, faulty response.
- Covers all parts of PikaNetwork's API (https://stats.pika-network.net/api)


Credits
-------

- Author: [sti1ltyping](https://discord.com/users/840587974000771072)
- Contact: https://discord.gg/B3DQgwUgyT

- This API wrapper is developed by the dedicated development team of  [`Pikachu's Stats`](https://discord.com/oauth2/authorize?client_id=1112768481956479108&permissions=563914781097033&scope=bot). This same wrapper is utilized within the application.

EXAMPLES
====


1. Profile and Stats


```python
from PikaPY import Pikanetwork, PikaAnnotations
import asyncio


async def main():

    # Sending API requests with an asynchronous environment
    async with Pikanetwork() as api:

        profile = await api.Profile('Fireor')
        stats = await api.Stats('Fireor', "bedwars", "total", "all_modes")
    
    # Extracting items from the response
    username = profile.username
    rank = profile.highest_minigame_rank
    level = profile.level
    last_seen = profile.last_seen_text

    # Extracting guild from player's profile
    guild = profile.guild()

    # Assigning variables if player is not in a guild
    if guild is None:
        guild_name = None
        guild_tag = None
        guild_owner = None
        guild_level = None
        guild_mc = None
    
    guild_name = guild.name
    guild_tag = guild.tag
    guild_owner = guild.leader
    guild_level = guild.level
    guild_mc = guild.member_count

    # Extracting stats
    wins = stats.wins
    wins_lb = stats.wins_lb

    losses = stats.losses
    losses_lb = stats.losses

    wlr = stats.wlr
    win_rate = stats.win_rate
    
    # creating a templet to output
    description = f"""
    {username}'s Stats [{rank}]

    level: {level}
    last seen: {last_seen}

    Guild:
        Name: {guild_name}
        Tag: {guild_tag}
        Leader: {guild_owner}
        level: {guild_level}
        Members: {guild_mc}

    Stats:
        Wins: {wins} | #{wins_lb}
        Losses: {losses} | #{losses_lb}

        wlr: {wlr}
        win rate: {win_rate}%
    """
    print(description)


asyncio.run(main())
```


2. Guilds


```python
from PikaPY import Pikanetwork, PikaAnnotations
import asyncio


async def main():

    # Sending API requests with an asynchronous environment
    async with Pikanetwork() as api:

        guild = await api.Guild("RIP")
    
    # If guild doesn't exists
    if guild is None:
        print("Guild not found!")
        return
    
    # Extracting items from the response
    guild_created_at = guild.created_at # UnixTimestamp usable in discord timestamp(<t:UnixTimestamp:R>)
    guild_name = guild.name
    guild_tag = guild.tag
    guild_owner = guild.leader
    guild_level = guild.level
    guild_member_count = guild.member_count

    guild_members = guild.member_list

    
    # creating a templet to output
    description = f"""
    Guild [<t:{guild_created_at}:R>]:

        Name: {guild_name}
        Tag: {guild_tag}
        Leader: {guild_owner}
        level: {guild_level}
        Members: {guild_member_count}

        list: {guild_members}
    """
    print(description)


asyncio.run(main())
```


3. Recaps


```python
from PikaPY import Pikanetwork, PikaAnnotations
import asyncio


async def main():

    # Sending API requests with an asynchronous environment
    async with Pikanetwork() as api:

        recap = await api.Recap("c19218da-69fc-4c27-99f6-c607c1676ac2")
    
    # If recap doesn't exists
    if recap is None:
        print("Recap not found!")
        return
    
    # Extracting items from the response
    recap_id = recap.id
    winners = ', '.join(winner for winner in recap.winners)
    most_kills = recap.most_kills
    player_with_most_kills = recap.player_with_most_kills
    mapname = recap.map_name
    started = recap.game_start # UnixTimestamp
    duration = recap.game_duration
    link = recap.recap_link
    players = ", ".join(player for player in recap.players)
    
    # creating a templet to output
    description = f"""
    Recap: {recap_id} | Game started: <:t{started}:F> | Duration: {duration}:
    link: {link}

        winners: {winners}
        map: {mapname}
        most kills: {player_with_most_kills} | {most_kills}

        players: {players}
    """
    print(description)


asyncio.run(main())
```


4. MultiProcessing


```python
from PikaPY import Pikanetwork, PikaAnnotations
import asyncio

# PikaPY automates batch processing.
# No matter how big the lists are it will automatically break it into batches and fetch the responses.
players = ["Fireor", "fwgazes", "ignLone"]
guilds = ["RIP", "EKITTENS", "Menace"]

async def main():

    # Sending API requests with an asynchronous environment
    async with Pikanetwork() as api:

        _profiles = await api.MultiProfile(api, players)
        _stats = await api.MultiStats(api, players, "bedwars", "total", "all_modes")
        _guilds = await api.MultiGuilds(api, guilds)
    
    
    # Multi-Processing always returns response in the form of ("object's name", 'API Response')
    for player, profile in _profiles:
        
        player: str
        profile: PikaAnnotations.Profile

        if profile is None:
            print(f'Couldn\'t find any player named {player}!')

        print(player, profile.level)

    for player, stats in _stats:
        
        player: str
        stats: PikaAnnotations.Stats

        if profile is None:
            print(f'Couldn\'t find any player named {player}!')

        print(player, stats.wins)

    for name, guild in _guilds:
        
        name: str
        guild: PikaAnnotations.Guild

        if profile is None:
            print(f'Couldn\'t find any guild named {name}!')

        print(name, guild.totalexp)


asyncio.run(main())
```