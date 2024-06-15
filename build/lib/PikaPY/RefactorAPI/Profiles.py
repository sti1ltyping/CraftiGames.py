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

from .Guilds import Guild
from PikaPY.utils import imports, UnixTimestamp # type: ignore
from PikaPY.Skins import SkinTypes # type: ignore

class Profile:
    """
    Wrap Profile
    ~~~~~

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

    def __init__(self, data: dict, session: imports.aiohttp.ClientSession):
        self.raw: dict = data
        self.session = session

    @property
    def skin(self) -> SkinTypes:
        return SkinTypes(self.username, self.session)
    
    @property
    def discord_verified(self) -> bool:
        """
        Returns:
        - `true` if player has connected with discord account.
        - `false` if player has not connected with discord account.
        """
        return self.raw.get("discord_verified", False)
    
    @property
    def discord_boosting(self) -> bool:
        """
        Returns:
        - `true` if player has boosted `PikaNetwork`'s official discord server.
        - `false` if player has not boosted `PikaNetwork`'s official discord server.
        """
        return self.raw.get("discord_boosting", False)
    
    @property
    def email_verified(self) -> bool:
        """
        Returns:
        - `true` if player has connected with email.
        - `false` if player has not connected with email.
        """
        return self.raw.get("email_verified", False)

    @property
    def username(self) -> str:
        """
        Returns:
        - username of the player.
        """
        return self.raw.get("username", '')
    
    @property
    def link(self) -> str:
        """
        Returns:
        - PikaNetwork link to the player's profile.
        """
        return f"https://stats.pika-network.net/player/{self.username}"
    
    @property
    def level(self) -> int:
        """
        Returns:
        - Level of the player.
        """
        return int(self.raw.get("rank", {}).get("level", 0))
    
    @property
    def level_percentage(self) -> float:
        """
        Returns:
        - level percentage of the player.
        """
        return float(self.raw.get("rank", {}).get("percentage", 0))
    
    @property
    def highest_minigame_rank(self) -> imports.Literal[
        "Developer", # 0
        "Admin",     # 1
        "Manager",   # 2
        "SrMod",     # 3
        "Moderator", # 4
        "Helper",    # 5
        "Trial",     # 6
        "Youtuber",  # 7
        "Champion",  # 8
        "Titan",     # 9
        "Elite",     # 10
        "VIP",       # 11
        "Unranked"   # 12 (Unranked)
        ]:
        """
        Returns:
        - Highest minigame rank of the player.
        """
        try:
            sorted_ranks = sorted(self.raw.get("ranks", []), key=lambda x: {
                "developer": 0, "admin": 1,"manager": 2, "srmod": 3, "moderator": 4, "helper": 5, "trial": 6, "youtuber": 7, "champion": 8, "titan": 9, "elite": 10, "vip": 11
                }.get(x.get('displayName', '').lower(), float('inf')))
            check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
            if check.lower() in ["developer", "admin", "manager", "srmod", "moderator", "helper", "trial", "youtuber", "champion", "titan", "elite", "vip"]:
                return check
            else:
                return 'Unranked'
        except Exception:
            return 'Unranked'
    
    @property
    def highest_practice_rank(self) -> imports.Literal[
        "Emerald", # 0
        "Diamond", # 1
        "Gold",    # 2
        "Silver",  # 3
        "Unranked" # 4
        ]:
        """
        Returns:
        - Highest practice rank of the player.
        """
        try:
            sorted_ranks = sorted(self.raw.get("ranks", []), key=lambda x: {
                "emerald": 0,"diamond": 1, "gold": 2, "silver": 3
            }.get(x.get('displayName', '').lower(), float('inf')))
            check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
            if check.lower() in ["emerald","diamond", "gold", "silver"]:
                return check
            else:
                return 'Unranked'
        except Exception:
            return 'Unranked'
        
    @property
    def last_seen(self) -> UnixTimestamp:
        """
        Returns:
        - UnixTimestamp (usable in discord timestamp) of player's last seen date-time.
        """
        last_seen_raw: int | None = self.raw.get("lastSeen", None)
        return int(imports.time.time()) if last_seen_raw == -1 or last_seen_raw is None else int(str(last_seen_raw)[:-3]) # Staffs have -1
    
    @property
    def last_seen_text(self) -> (str | None):
        """
        Returns:
        - last seen value in text format.
        """
        try:

            time_difference = imports.datetime.utcnow() - imports.datetime.utcfromtimestamp(self.last_seen)

            if time_difference.days > 0:
                return "1 day ago" if time_difference.days == 1 else f"{time_difference.days} days ago"
                    
            elif time_difference.seconds < 60:
                return "just now"
            
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                return "1 min ago" if minutes == 1 else f"{minutes} mins ago"
            
            else:
                hours = time_difference.seconds // 3600
                return "1 hr ago" if hours == 1 else f"{hours} hrs ago"

        except Exception:
            return None
        
    @property
    def friend_list(self) -> list | None:
        """
        Returns:
        - List of player's friends. (iterable in ascending order)
        - None if the list is empty.
        """
        all_friends = self.raw.get('friends', [])
        friends = sorted([user['username'] for user in all_friends])

        return friends if friends else None
        
    @property
    def friend_count(self) -> int:
        """
        Returns:
        - Number of friends of the player.
        """
        frineds = self.friend_list
        return 0 if frineds is None else len(frineds)
    
    @property
    def is_staff(self) -> bool:
        """
        Returns:
        - `True` if player is part of the staff team.
        - `False` if player is not a staff.
        """
        return True if self.highest_minigame_rank.lower() in ["developer", "admin", "manager", "srmod", "moderator", "helper", "trial"] else False
    
    def guild(self) -> (Guild | None):
        """
        Extract guild from player's profile.
        
        Return:
        - Guild (class).
        - None if guild is not found.
        """
        clan = self.raw.get("clan", None)
        return None if clan is None else Guild(clan)