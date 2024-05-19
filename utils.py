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

class imports:
    import aiohttp
    import json
    import asyncio
    import time
    from datetime import (
        datetime,
        timedelta
    )
    from bs4 import BeautifulSoup
    import traceback
    import random


class Weekly:

    """Represents weekly interval."""
    def __str__(self):
        return "weekly"
    
class Monthly:

    """Represents monthly interval."""
    def __str__(self):
        return "monthly"
    
class Yearly:
    
    """Represents yearly interval."""
    def __str__(self):
        return "yearly"
    
class Total:

    """Represents all times."""
    def __str__(self):
        return "total"

class All_Modes:

    """Represents all_modes."""
    def __str__(self):
        return "all_modes"
    
class Solo:

    """Represents solo gamemode."""
    def __str__(self):
        return "solo"
    
class Doubles:

    """Represents doubles mode."""
    def __str__(self):
        return "doubles"
    
class Triples:

    """Represents triples mode."""
    def __str__(self):
        return "triples"
    
class Quadriples:

    """Represents quadriples modes."""
    def __str__(self):
        return "quad"

class Gamemodes:

    """List of available gamemodes"""
    
    def bedwars():
        return "bedwars"
    
    def skywars():
        return "skywars"
    
    def unrankedpractice():
        return "unrankedpractice"
    
    def rankedpractice():
        return "rankedpractice"
    
    def all() -> list:
        return ['bedwars', 'skywars', 'unrankedpractice', 'rankedpractice']
    
class Intervals:

    """List of available intervals"""
    
    def weekly():
        return "weekly"
    
    def monthly():
        return "monthly"
    
    def yearly():
        return "yearly"
    
    def total():
        return "total"
    
    def all() -> list:
        return ['weekly', 'monthly', 'yearly', 'total']

class Modes:

    """List of available modes"""

    def all_modes():
        return "ALL_MODES"
    
    def SOLO():
        return "SOLO"
    
    def doubles():
        return "DOUBLES"
    
    def triples():
        return "TRIPLES"
    
    def quad():
        return "QUAD"
    
    def all() -> list:
        return ['ALL_MODES', 'SOLO', 'DOUBLES', 'TRIPLES', 'QUAD']
    

    

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/97.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.1072.62 Safari/537.36'
]

device_ids = [
    '0123456789abcdef',
    '9876543210abcdef',
    'abcdef0123456789',
    '1234567890abcdef',
    '4567890123abcdef'
]


async def header() -> {imports.aiohttp.ClientSession.headers}:

    headers = {
            'User-Agent': imports.random.choice(user_agents),
            'Device-Id': imports.random.choice(device_ids)
        }
    
    return headers


with open("settings.json", "r") as file:
    data: dict = imports.json.load(file)

    Allowed_Recursion: int = data.get("Allowed Recursion", 30)
    batch_size: int = data.get("Batch size", 10)


if __name__ == '__main__':
    imports.asyncio.run(header())