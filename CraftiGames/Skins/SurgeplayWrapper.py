"""
MIT License

Copyright (c) 2024 sti1ltyping
...
"""

from CraftiGames.utils import packages  # type: ignore
from CraftiGames.utils import config  # type: ignore

default_skins = config.default_skins
BASE_URL = "https://visage.surgeplay.com"
MOJANG_API_URL = "https://api.mojang.com/users/profiles/minecraft"
MAX_RETRIES = 5
DEFAULT_SIZE = 300


class BaseSkinRender:
    """Base class for skin rendering with retry logic."""

    def __init__(self, player: str, session: packages.aiohttp.ClientSession, size: int = DEFAULT_SIZE) -> None:
        self.player: str = player
        self.session: packages.aiohttp.ClientSession = session
        self.size: int = size
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

        print("\n===== RESOLVING PLAYER =====")
        print("Original:", repr(player))

        is_uuid = (
            len(player) == 32 and all(c in "0123456789abcdefABCDEF" for c in player)
        ) or (
            len(player) == 36
            and player[8] == "-"
            and player[13] == "-"
            and player[18] == "-"
            and player[23] == "-"
        )

        print("Already UUID:", is_uuid)

        if not is_uuid:
            uuid = await self.username_to_uuid(player, self.session)

            print("Mojang UUID:", uuid)

            if uuid:
                self.player = (
                    f"{uuid[0:8]}-"
                    f"{uuid[8:12]}-"
                    f"{uuid[12:16]}-"
                    f"{uuid[16:20]}-"
                    f"{uuid[20:32]}"
                )

        print("Resolved:", repr(self.player))
        print("===========================\n")

    async def _fetch_image(self, url: str) -> (packages.BytesIO | None):
        try:
            print("\n===== VISAGE REQUEST =====")
            print("Player:", repr(self.player))
            print("URL:", repr(url))

            headers = {
                "User-Agent": "CraftiGames/1.0 (+https://github.com/sti1ltyping/CraftiGames)"
            }

            async with self.session.get(
                url,
                headers=headers,
                allow_redirects=True,
                timeout=packages.aiohttp.ClientTimeout(total=10)
            ) as response:

                print("Status:", response.status)
                print("Final URL:", response.url)
                print("Content-Type:", response.headers.get("Content-Type"))

                if response.status == 200:
                    data = await response.read()

                    print("Image Size:", len(data), "bytes")
                    print("=========================\n")

                    self.retry_count = 0
                    return packages.BytesIO(data)

                print("===== ERROR RESPONSE =====")

                try:
                    error_text = await response.text(errors="replace")
                    print(error_text)
                except Exception:
                    error_bytes = await response.read()
                    print(error_bytes[:500])

                print("==========================")

                if response.status in (400, 404, 500):
                    return await self._retry_with_default(url)

                return None

        except Exception as e:
            print("===== EXCEPTION =====")
            print(type(e).__name__, str(e))
            print("=====================")

            return await self._retry_with_default(url)

    async def _retry_with_default(self, url: str) -> (packages.BytesIO | None):
        self.retry_count += 1

        if self.retry_count >= MAX_RETRIES:
            print("Max retries reached.")
            return None

        fallback_player = packages.random.choice(default_skins)

        print(f"\n===== FALLBACK RETRY #{self.retry_count} =====")
        print("Original URL:", url)
        print("Fallback Player:", fallback_player)

        self.player = fallback_player

        await self._resolve_player()

        url_parts = url.split("/")
        url_parts[-1] = self.player

        new_url = "/".join(url_parts)

        print("Retry URL:", new_url)
        print("===============================\n")

        return await self._fetch_image(new_url)


class SkinTypes:
    """
    Wraps Skins using the Visage API (https://visage.surgeplay.com).

    Supported render types:
        Face, Head, Bust, Full, Player, Helm, Portrait, Front, FrontFull,
        Skin, ProcessedSkin

    MIT License
    Copyright (c) 2024 sti1ltyping
    """

    def __init__(self, player: str, session: packages.aiohttp.ClientSession, size: int = DEFAULT_SIZE) -> None:
        self.player: str = player
        self.session: packages.aiohttp.ClientSession = session
        self.size: int = size

        self.Face          = self.Face(self.player, self.session, self.size)
        self.Head          = self.Head(self.player, self.session, self.size)
        self.Bust          = self.Bust(self.player, self.session, self.size)
        self.Full          = self.Full(self.player, self.session, self.size)
        self.Player        = self.Player(self.player, self.session, self.size)
        self.Helm          = self.Helm(self.player, self.session, self.size)
        self.Portrait      = self.Portrait(self.player, self.session, self.size)
        self.Front         = self.Front(self.player, self.session, self.size)
        self.FrontFull     = self.FrontFull(self.player, self.session, self.size)
        self.Skin          = self.Skin(self.player, self.session, self.size)
        self.ProcessedSkin = self.ProcessedSkin(self.player, self.session, self.size)

    class Face(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/face/{self.size}/{self.player}")

    class Head(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/head/{self.size}/{self.player}")

    class Bust(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/bust/{self.size}/{self.player}")

    class Full(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/full/{self.size}/{self.player}")

    class Player(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/player/{self.size}/{self.player}")

    class Helm(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/helm/{self.size}/{self.player}")

    class Portrait(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/portrait/{self.size}/{self.player}")

    class Front(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/front/{self.size}/{self.player}")

    class FrontFull(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/frontfull/{self.size}/{self.player}")

    class Skin(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/skin/{self.player}")

    class ProcessedSkin(BaseSkinRender):
        async def render(self) -> (packages.BytesIO | None):
            await self._resolve_player()
            return await self._fetch_image(f"{BASE_URL}/processedskin/{self.player}")