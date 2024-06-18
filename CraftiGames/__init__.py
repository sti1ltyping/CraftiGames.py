# Author: sti1ltyping
# Discord: sti1ltyping | ID: 840587974000771072
# Contact: https://discord.gg/B3DQgwUgyT

# THIS API WRAPPER IS MADE BY DEVELOPERS OF Pikachu's Stats#1210 (1112768481956479108)
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

__title__ = 'CraftGames'
__author__ = 'sti1ltyping'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2024 sti1ltyping'
__version__ = '1.1.1'

from typing import NamedTuple, Literal

from .__PikaNetwork__ import (
    Pikanetwork,
    PikaAnnotations,
)

from .__JartexNetwork__ import (
    Jartexnetwork,
    JartexAnnotations
)

from .utils import (
    APIResponseError,
    APIBlockedException
)

from .utils import config


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0,
    minor=0,
    micro=3,
    release="beta",
    serial=0
)

del NamedTuple, Literal, VersionInfo