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
    from io import BytesIO
    import traceback
    import random
    from typing import (
        Literal, Union
    )
    from dateutil import parser
    import configparser


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
    
    @property
    def bedwars():
        return "bedwars"
    
    @property
    def skywars():
        return "skywars"
    
    @property
    def unrankedpractice():
        return "unrankedpractice"
    
    @property
    def rankedpractice():
        return "rankedpractice"
    
    def all() -> list:
        return ['bedwars', 'skywars', 'unrankedpractice', 'rankedpractice']
    
class Intervals:

    """List of available intervals"""
    
    @property
    def weekly():
        return "weekly"
    
    @property
    def monthly():
        return "monthly"
    
    @property
    def yearly():
        return "yearly"
    
    @property
    def total():
        return "total"
    
    def all() -> list:
        return ['weekly', 'monthly', 'yearly', 'total']

class Modes:

    """List of available modes"""
    
    @property
    def all_modes():
        return "ALL_MODES"
    
    @property
    def solo():
        return "SOLO"
    
    @property
    def doubles():
        return "DOUBLES"
    
    @property
    def triples():
        return "TRIPLES"
    
    @property
    def quad():
        return "QUAD"
    
    def all() -> list:
        return ['ALL_MODES', 'SOLO', 'DOUBLES', 'TRIPLES', 'QUAD']
    

class APIResponseError(Exception):
    """Raise error on API's host side issue."""
    def __init__(self, message="API is not responding to the requests."):
        self.message = message
        super().__init__(self.message)

class APIBlockedException(Exception):
    """Exception raised when the API requests are blocked."""
    def __init__(self, message="API requests are being blocked."):
        self.message = message
        super().__init__(self.message)
    
class Do_Not_Touch: ...

class UnixTimestamp: ...

class aiohttpClientHeader:
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/97.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.1072.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.4.11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5173.13 Safari/537.36'
    ]

    device_ids = [
        '0123456789abcdef',
        '9876543210abcdef',
        'abcdef0123456789',
        '1234567890abcdef',
        '4567890123abcdef',
        'feedfacecafebeef',
        'deadbeef12345678',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '9a8b7c6d5e4f3g2h',
        '0123456789abcdef',
        '9876543210abcdef',
        'abcdef0123456789',
        '1234567890abcdef',
        '4567890123abcdef',
        'feedfacecafebeef',
        'deadbeef12345678',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c'
    ]


async def header() -> aiohttpClientHeader:
    headers = {
        'User-Agent': imports.random.choice(aiohttpClientHeader.user_agents),
        'Device-Id': imports.random.choice(aiohttpClientHeader.device_ids)
    }
    return headers


class Check:

    valid_modes = {
        'Bedwars': [
            'all_modes',
            'solo',
            'doubles',
            'triples',
            'quad'
        ],

        'Skywars': [
            'all_modes',
            'solo',
            'doubles'
        ],

        'Practice': [
            'all_modes'
        ]
    }

    allowed_stats = {
        'Bedwars': [
            'wins',
            'losses',

            'kills',
            'deaths',

            'final_kills',
            'final_deaths',
            'bed_destroyed',

            'melee_kills',
            'void_kills',

            'bow_kills',
            'arrows_hit',
            'arrows_shot',

            'played',
            'highest_win_streak',
        ],
        
        'Skywars': [
            'wins',
            'losses',

            'kills',
            'deaths',

            'melee_kills',
            'void_kills',

            'bow_kills',
            'arrows_hit',
            'arrows_shot',

            'played',
            'highest_win_streak',
        ],

        'UnrankedPractice': [
            'wins',
            'losses',

            'kills',

            'projectile_kills',
            'melee_dealt',
            'melee_taken',
            
            'void_kills',
            'played',
            'highest_win_streak',
        
        ],

        'RankedPractice': [
            'wins',
            'losses',

            'kills',

            'projectile_kills',
            'melee_dealt',
            'melee_taken',

            'void_kills',
            'played',
            'highest_win_streak',
            'elo'
        ]

    }
    def __init__(self) -> None:
        self.valid_modes_in_skywars = self.valid_modes.get('Skywars')
        self.valid_modes_in_practice = self.valid_modes.get('Practice')

        self.Bedwars = self.allowed_stats.get('Bedwars')
        self.Skywars = self.allowed_stats.get('Skywars')
        self.UnrankedPractice = self.allowed_stats.get('UnrankedPractice')
        self.RankedPractice = self.allowed_stats.get('RankedPractice')

    def __stats_input__(
            self,
            gamemode: str,
            interval: str,
            mode: str
            ) -> None:
        
        
        if gamemode not in Gamemodes.all():
            raise ValueError('Invalid gamemode has been passed!')
        elif interval not in Intervals.all():
            raise ValueError('Invalid interval has been passed!')
        elif mode not in Modes.all():
            raise ValueError('Invalid mode has been passed!')
        
        if gamemode.lower() == 'skywars' and mode.lower() not in self.valid_modes_in_skywars:
            raise ValueError("Invalid mode, can\'t use that in skywars. Can only use solo or doubles.")
        elif gamemode.lower() in ['rankedpractice', 'unrankedpractice'] and mode.lower() not in self.valid_modes_in_practice:
            raise ValueError("Invalid mode, can't use that in practice. Can only use all_modes.")
        
    def __leaderboard_input__(
            self,
            gamemode: str,
            interval: str,
            mode: str,
            stats: str
            ) -> None:
        if gamemode.lower() not in Gamemodes.all():
            raise ValueError('Invalid gamemode has been passed!')
        elif interval.lower() not in Intervals.all():
            raise ValueError('Invalid interval has been passed!')
        elif mode.upper() not in Modes.all():
            raise ValueError('Invalid mode has been passed!')
        elif stats.lower() not in self.Bedwars and stats not in self.Skywars and stats not in self.UnrankedPractice and stats not in self.RankedPractice:
            raise ValueError('Invalid stats has been passed!')
        
        if gamemode.lower() == 'skywars' and mode.lower() not in self.valid_modes_in_skywars:
            raise ValueError("Invalid mode, can't use that in skywars. Can only use solo or doubles.")
        elif gamemode.lower() in ['rankedpractice', 'unrankedpractice'] and mode.lower() not in self.valid_modes_in_practice:
            raise ValueError("Invalid mode, can't use that in practice. Can only use all_modes.")
        
        if gamemode.lower() == 'bedwars' and stats.lower() not in self.Bedwars:
            raise ValueError("Invalid stats, you can't use that in bedars.")
        elif gamemode.lower() == 'skywars' and stats.lower() not in self.Skywars:
            raise ValueError("Invalid stats, you can't use that in skywars.")
        elif gamemode.lower() == 'rankedpractice' and stats.lower() not in self.RankedPractice:
            raise ValueError("Invalid stats, you can't use that in rankedpractice.")
        elif gamemode.lower() == 'unrankedpractice' and stats.lower() not in self.UnrankedPractice:
            raise ValueError("Invalid stats, you can't use that in unrankedpractice.")


config = imports.configparser.ConfigParser()
config.read('PikaPY/settings.ini')

logging = config.getboolean('DEFAULT', 'Logging', fallback=False)
Allowed_Recursion = config.getint('DEFAULT', 'Allowed_Recursion', fallback=30)
batch_size = config.getint('DEFAULT', 'Batch_size', fallback=10)

default_skins = config.get('Skins', 'Default', fallback="XSteve").split(',')

delay_after_exceeding_ratelimit = config.getfloat('Ratelimit', 'Delay_After_Exceeding_Ratelimit', fallback=1.5)
batch_delay = config.getfloat('Ratelimit', 'Delay_Between_Batches', fallback=1)
Interval = config.getint('Ratelimit','Interval', fallback=1)
MAX_REQUESTS_PER_INTERVAL = config.getint('Ratelimit','Request_Per_Interval', fallback=20)
delay = config.getfloat('Ratelimit','Delay', fallback=1.5)