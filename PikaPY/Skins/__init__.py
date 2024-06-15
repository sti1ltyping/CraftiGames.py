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

from PikaPY.utils import imports # type: ignore
from PikaPY.utils import default_skins # type: ignore


class SkinTypes:
    """
    Wraps Skins
    ~~~~~~~~~~

    ==================================================================================================

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
    SOFTWARE."""
    
    def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
        self.player: str = player
        self.session: imports.aiohttp.ClientSession = session

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

    class Default:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Default bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/default/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Default full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/default/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Default face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/default/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Marching:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Marching bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/marching/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Marching full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/marching/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Marching face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/marching/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None


    class Walking:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Walking bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/walking/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Walking full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/walking/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Walking face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/walking/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None

    
    class Crouching:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Crouching bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crouching/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Crouching full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crouching/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Crouching face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crouching/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Crossed:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Crossed bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crossed/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Crossed full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crossed/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Crossed face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/crossed/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Criss_cross:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Criss cross bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/criss_cross/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Criss cross full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/criss_cross/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Criss cross face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/criss_cross/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                
    
    class Ultimate:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Ultimate bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/ultimate/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Ultimate full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/ultimate/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Ultimate face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/ultimate/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Isometric:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Isometric bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/isometric/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Isometric full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/isometric/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Isometric face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/isometric/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                
        async def head(self) -> (imports.BytesIO | None):
            """
            Isometric head image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/isometric/{self.player}/head') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                
    
    class Head:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self
        

        async def full(self) -> (imports.BytesIO | None):
            """
            Head image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/head/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
                
    
    class Custom:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Custom bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/custom/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Custom full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/custom/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Custom face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/custom/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Cheering:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Cheering bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cheering/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Cheering full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cheering/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Cheering face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cheering/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Relaxing:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Relaxing bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/relaxing/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Relaxing full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/relaxing/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Relaxing face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/relaxing/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                
    
    class Trudging:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Trudging bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/trudging/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Trudging full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/trudging/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Trudging face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/trudging/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Cowering:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Cowering bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cowering/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Cowering full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cowering/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Cowering face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/cowering/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Pointing:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Pointing bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pointing/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Pointing full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pointing/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Pointing face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pointing/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Lunging:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Lunging bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/lunging/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Lunging full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/lunging/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Lunging face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/lunging/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                
    
    class Dungeons:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Dungeons bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dungeons/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Dungeons full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dungeons/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Dungeons face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dungeons/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
        
    
    class Facepalm:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Facepalm bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/facepalm/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Facepalm full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/facepalm/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Facepalm face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/facepalm/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Sleeping:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Sleeping bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/sleeping/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Sleeping full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/sleeping/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
                

    class Dead:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Dead bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dead/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Dead full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dead/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Dead face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/dead/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Archer:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Archer bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/archer/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Archer full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/archer/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Archer face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/archer/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
        

    class Kicking:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Kicking bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/kicking/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Kicking full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/kicking/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Kicking face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/kicking/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Mojavatar:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Mojavatar bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/mojavatar/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Mojavatar full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/mojavatar/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
                

    class Reading:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Reading bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/reading/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Reading full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/reading/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Reading face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/reading/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Bitzel:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Bitzel bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/bitzel/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Bitzel full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/bitzel/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Bitzel face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/bitzel/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Pixel:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def bust(self) -> (imports.BytesIO | None):
            """
            Pixel bust image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pixel/{self.player}/bust') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.bust()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.bust()
                
                else:
                    return None

        async def full(self) -> (imports.BytesIO | None):
            """
            Pixel full image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pixel/{self.player}/full') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.full()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.full()
                
                else:
                    return None
        
        async def face(self) -> (imports.BytesIO | None):
            """
            Pixel face image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/pixel/{self.player}/face') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.face()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.face()
                
                else:
                    return None
                

    class Skin:
        def __init__(self, player: str, session: imports.aiohttp.ClientSession) -> None:
            self.player: str = player
            self.session: imports.aiohttp.ClientSession = session
            self.Retry = 0

        async def __cracked__(self):
            self.Retry += 1
            if self.Retry >= 5:
                self = None
            self.player = imports.random.choice(default_skins)
            return self

        async def default(self) -> (imports.BytesIO | None):
            """
            Skin of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/skin/{self.player}/default') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.default()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.default()
                
                else:
                    return None

        async def processed(self) -> (imports.BytesIO | None):
            """
            Processed image of the player.

            Returns:
            - Image Bytes of the skin of the player.
            - Image Bytes of the default skin as player is not premium.
            - None if something went wrong.
            """
            async with self.session.get(f'https://starlightskins.lunareclipse.studio/render/skin/{self.player}/processed') as response:

                if response.status == 200:
                    try:
                        self.Retry = 0
                        return imports.BytesIO(await response.read())
                    
                    except Exception:
                        self = await self.__cracked__()
                        return None if self is None else await self.processed()
                    
                elif response.status == 500:

                    self = await self.__cracked__()
                    return None if self is None else await self.processed()
                
                else:
                    return None