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

from .Guilds import Guild
from PikaPY.utils import imports # type: ignore
from PikaPY.Skins import SkinTypes # type: ignore

class Profile:
    """
    Wrap Profile
    ~~~~~

    ==================================================================================================

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
    SOFTWARE."""

    def __init__(self, data, session):
        self.data: dict = data
        self.session = session

    async def connections(self) -> tuple[bool, bool, bool]:
        """
        Returns:
        - status (bool) of discord account, server boosting and email connection
        """
        return self.data.get("discord_verified"), self.data.get("discord_boosting"), self.data.get("email_verified")

    async def username(self) -> str:
        """
        Returns:
        - username of the player.
        """
        return self.data.get("username")
        
    async def level(self) -> int:
        """
        Returns:
        - Level of the player.
        """
        return int(self.data.get("rank", {}).get("level", 0))
        
    async def level_percentage(self) -> float:
        """
        Returns:
        - level percentage of the player.
        """
        return float(self.data.get("rank", {}).get("percentage", 0))
        
    async def highest_minigame_rank(self) -> (str | imports.Literal['Unranked']):
        """
        Returns:
        - Highest minigame rank of the player.
        """
        sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
            "developer": 0, "admin": 1,"manager": 2, "srmod": 3, "moderator": 4, "helper": 5, "trial": 6, "youtuber": 7, "champion": 8, "titan": 9, "elite": 10, "vip": 11
            }.get(x.get('displayName', '').lower(), float('inf')))
        check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
        if check.lower() in ["developer", "admin", "manager", "srmod", "moderator", "helper", "trial", "youtuber", "champion", "titan", "elite", "vip"]:
            return check
        else:
            return 'Unranked'
        
    async def highest_practice_rank(self) -> (str | imports.Literal['Unranked']):
        """
        Returns:
        - Highest practice rank of the player.
        """
        sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
            "emerald": 0,"diamond": 1, "gold": 2, "silver": 3
        }.get(x.get('displayName', '').lower(), float('inf')))
        check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
        if check.lower() in ["emerald","diamond", "gold", "silver"]:
            return check
        else:
            return 'Unranked'
        
    async def last_seen(self) -> int:
        """
        Returns:
        - Last seen value discord format.
        """
        last_seen_raw = self.data.get("lastSeen")
        if last_seen_raw == -1:
            return int(imports.time.time()) # Staff's have -1
        last_seen = str(last_seen_raw)[:-3]
        return int(last_seen)
    
    async def last_seen_text(self) -> imports.Union[str, None]:
        """
        Returns:
        - last seen value in text format.
        """
        try:
            last_seen_timestamp = await self.last_seen()
            last_seen_datetime = imports.datetime.utcfromtimestamp(last_seen_timestamp)

            current_datetime = imports.datetime.utcnow()
            time_difference = current_datetime - last_seen_datetime

            if time_difference.days > 0:
                if time_difference.days == 1:
                    return "1 day ago"
                else:
                    return f"{time_difference.days} days ago"
            elif time_difference.seconds < 60:
                return "just now"
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                if minutes == 1:
                    return "1 min ago"
                else:
                    return f"{minutes} mins ago"
            else:
                hours = time_difference.seconds // 3600
                if hours == 1:
                    return "1 hr ago"
                else:
                    return f"{hours} hrs ago"
        except Exception as e:
            return None
        
    async def friend_list(self) -> imports.Union[list, None]:
        """
        Returns:
        - List of player's friends. 
        - None if no friends found.
        """
        friends_raw = self.data.get('friends', [])
        friends = [user['username'] for user in friends_raw]

        if not friends_raw:
            return None
        return friends
        
    async def friend_count(self) -> int:
        """
        Returns:
        - Friend count.
        - None if no friends found.
        """
        frineds = await self.friend_list()
        if frineds is None:
            return 0
        return len(frineds)
        
    async def guild(self) -> imports.Union[Guild, None]:
        """
        Fetch guild of the player.
        
        Return:
        - Guild (class).
        - None if guild is not found.
        """
        clan = self.data.get("clan", None)
        if clan is None:
            return None
        return Guild(clan)
    
    async def raw(self) -> dict:
        """
        Returns:
        - Raw data.
        """
        return self.data
    
    async def SkinsVarieties(self) -> SkinTypes:
        """
        Return:

        - All available skins. 
        """
        return SkinTypes(await self.username(), self.session)