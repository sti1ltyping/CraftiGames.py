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



EXAMPLES
====


1. General Profile and Stats


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
