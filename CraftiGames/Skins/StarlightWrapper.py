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

from CraftiGames.utils import packages  # type: ignore
from CraftiGames.utils import config  # type: ignore

default_skins = config.default_skins
BASE_URL = "https://starlightskins.lunareclipse.studio/render"
MOJANG_API_URL = "https://api.mojang.com/users/profiles/minecraft"
MAX_RETRIES = 5


class BaseSkinRender:
    """Base class for skin rendering with retry logic."""
    
    def __init__(self, player: str, session: packages.aiohttp.ClientSession) -> None:
        self.player: str = player
        self.session: packages.aiohttp.ClientSession = session
        self.retry_count: int = 0

    @staticmethod
    async def username_to_uuid(username: str, session: packages.aiohttp.ClientSession) -> (str | None):
        """
        Convert a Minecraft username to its UUID via the Mojang API.

        Returns:
        - UUID string (without hyphens) if the username exists
        - None if the username could not be resolved
        """
        try:
            async with session.get(
                f"{MOJANG_API_URL}/{username}",
                timeout=packages.aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("id")
                return None
        except Exception:
            return None

    async def _resolve_player(self) -> None:
        player = self.player
        is_uuid = (
            len(player) == 32 and all(c in "0123456789abcdefABCDEF" for c in player)
        ) or (
            len(player) == 36 and player[8] == "-" and player[13] == "-"
        )

        if not is_uuid:
            uuid = await self.username_to_uuid(player, self.session)
            if uuid:
                self.player = f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:32]}"

    async def _fetch_image(self, url: str) -> (packages.BytesIO | None):
        """
        Fetch an image from the given URL with fallback retry logic.

        Returns:
        - BytesIO object if successful
        - None if max retries exceeded
        """
        await self._resolve_player()

        try:
            async with self.session.get(url, timeout=packages.aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    self.retry_count = 0
                    return packages.BytesIO(await response.read())
                elif response.status == 500:
                    return await self._retry_with_default(url)
                else:
                    return None
        except Exception:
            return await self._retry_with_default(url)
    
    async def _retry_with_default(self, url: str) -> (packages.BytesIO | None):
        """Retry with a random default skin."""
        self.retry_count += 1
        
        if self.retry_count >= MAX_RETRIES:
            return None
        
        original_player = self.player
        self.player = packages.random.choice(default_skins)
        
        result = await self._fetch_image(url.rsplit('/', 1)[0] + '/' + self.player)
        
        if result is None:
            self.player = original_player
        
        return result


class SkinTypes:
    """
    Wraps Skins
    ~~~~~~~~~~

    MIT License

    Copyright (c) 2024 sti1ltyping
    ...
    """
    
    def __init__(self, player: str, session: packages.aiohttp.ClientSession) -> None:
        self.player: str = player
        self.session: packages.aiohttp.ClientSession = session

        self.Default = self.Default(self.player, self.session)
        self.Marching = self.Marching(self.player, self.session)
        self.Walking = self.Walking(self.player, self.session)
        self.Crouching = self.Crouching(self.player, self.session)
        self.Crossed = self.Crossed(self.player, self.session)
        self.Criss_cross = self.Criss_cross(self.player, self.session)
        self.Ultimate = self.Ultimate(self.player, self.session)
        self.Isometric = self.Isometric(self.player, self.session)
        self.Head = self.Head(self.player, self.session)
        self.Custom = self.Custom(self.player, self.session)
        self.Cheering = self.Cheering(self.player, self.session)
        self.Relaxing = self.Relaxing(self.player, self.session)
        self.Trudging = self.Trudging(self.player, self.session)
        self.Cowering = self.Cowering(self.player, self.session)
        self.Pointing = self.Pointing(self.player, self.session)
        self.Lunging = self.Lunging(self.player, self.session)
        self.Dungeons = self.Dungeons(self.player, self.session)
        self.Facepalm = self.Facepalm(self.player, self.session)
        self.Sleeping = self.Sleeping(self.player, self.session)
        self.Dead = self.Dead(self.player, self.session)
        self.Archer = self.Archer(self.player, self.session)
        self.Kicking = self.Kicking(self.player, self.session)
        self.Mojavatar = self.Mojavatar(self.player, self.session)
        self.Reading = self.Reading(self.player, self.session)
        self.Bitzel = self.Bitzel(self.player, self.session)
        self.Pixel = self.Pixel(self.player, self.session)
        self.Skin = self.Skin(self.player, self.session)

    class Default(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/default/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/default/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/default/{self.player}/face')

    class Marching(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/marching/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/marching/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/marching/{self.player}/face')

    class Walking(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/walking/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/walking/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/walking/{self.player}/face')

    class Crouching(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crouching/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crouching/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crouching/{self.player}/face')

    class Crossed(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crossed/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crossed/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/crossed/{self.player}/face')

    class Criss_cross(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/criss-cross/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/criss-cross/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/criss-cross/{self.player}/face')

    class Ultimate(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/ultimate/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/ultimate/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/ultimate/{self.player}/face')

    class Isometric(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/isometric/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/isometric/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/isometric/{self.player}/face')

    class Head(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/head/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/head/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/head/{self.player}/face')

    class Custom(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/custom/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/custom/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/custom/{self.player}/face')

    class Cheering(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cheering/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cheering/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cheering/{self.player}/face')

    class Relaxing(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/relaxing/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/relaxing/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/relaxing/{self.player}/face')

    class Trudging(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/trudging/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/trudging/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/trudging/{self.player}/face')

    class Cowering(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cowering/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cowering/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/cowering/{self.player}/face')

    class Pointing(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pointing/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pointing/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pointing/{self.player}/face')

    class Lunging(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/lunging/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/lunging/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/lunging/{self.player}/face')

    class Dungeons(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dungeons/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dungeons/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dungeons/{self.player}/face')

    class Facepalm(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/facepalm/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/facepalm/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/facepalm/{self.player}/face')

    class Sleeping(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/sleeping/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/sleeping/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/sleeping/{self.player}/face')

    class Dead(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dead/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dead/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/dead/{self.player}/face')

    class Archer(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/archer/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/archer/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/archer/{self.player}/face')

    class Kicking(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/kicking/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/kicking/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/kicking/{self.player}/face')

    class Mojavatar(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/mojavatar/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/mojavatar/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/mojavatar/{self.player}/face')

    class Reading(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/reading/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/reading/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/reading/{self.player}/face')

    class Bitzel(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/bitzel/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/bitzel/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/bitzel/{self.player}/face')

    class Pixel(BaseSkinRender):
        async def bust(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pixel/{self.player}/bust')
        async def full(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pixel/{self.player}/full')
        async def face(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/pixel/{self.player}/face')

    class Skin(BaseSkinRender):
        async def default(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/skin/{self.player}/default')
        async def processed(self) -> (packages.BytesIO | None):
            return await self._fetch_image(f'{BASE_URL}/skin/{self.player}/processed')