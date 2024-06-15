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
