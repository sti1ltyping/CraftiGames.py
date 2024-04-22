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

import aiohttp
import json
import asyncio
import time
from datetime import (
    datetime,
    timedelta
)


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

    def __repr__(self):
        return str(['bedwars', 'skywars', 'unrankedpractice', 'rankedpractice'])
    
class Intervals:

    """List of available intervals"""

    def __repr__(self):
        return str(['weekly', 'monthly', 'yearly', 'total'])

class Modes:

    """List of available modes"""

    def __repr__(self):
        return str(['ALL_MODES', 'SOLO', 'DOUBLES', 'TRIPLES', 'QUAD'])