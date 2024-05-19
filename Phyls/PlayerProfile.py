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

from .guilds import GUILD
from PikaPY.utils import imports # type: ignore

class Profile:
        
    """Wrap profile"""

    def __init__(self, data):
        self.data = data

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def connections(self) -> tuple:
        """Returns status of discord account, server boosting and email connection"""
        return self.data.get("discord_verified"), self.data.get("discord_boosting"), self.data.get("email_verified")

    async def username(self):
        """Returns username of the player.\n~~~"""
        return self.data.get("username")
        
    async def level(self) -> str:
        """Returns current level of the player.\n~~~"""
        return self.data.get("rank", {}).get("level")
        
    async def level_percentage(self) -> float:
        """Returns level percentage."""
        return float(self.data.get("rank", {}).get("percentage", 0))
        
    async def highest_minigame_rank(self):
        """Returns highest minigame rank of the player.\n~~~"""
        sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
            "developer": 0, "admin": 1,"manager": 2, "srmod": 3, "moderator": 4, "helper": 5, "trial": 6, "youtuber": 7, "champion": 8, "titan": 9, "elite": 10, "vip": 11
            }.get(x.get('displayName', '').lower(), float('inf')))
        check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
        if check.lower() in ["developer", "admin", "manager", "srmod", "moderator", "helper", "trial", "youtuber", "champion", "titan", "elite", "vip"]:
            return check
        else:
            return 'Unranked'
        
    async def highest_practice_rank(self):
        """Returns highest practice rank of the player.\n~~~"""
        sorted_ranks = sorted(self.data.get("ranks", []), key=lambda x: {
            "emerald": 0,"diamond": 1, "gold": 2, "silver": 3
        }.get(x.get('displayName', '').lower(), float('inf')))
        check = sorted_ranks[0]['displayName'] if sorted_ranks else 'Unranked'
        if check.lower() in ["emerald","diamond", "gold", "silver"]:
            return check
        else:
            return 'Unranked'
        
    async def last_seen(self) -> int:
        """Returns last seen value discord format."""
        last_seen_raw = self.data.get("lastSeen")
        last_seen = str(last_seen_raw)[:-3]
        return int(last_seen)
    
    async def last_seen_text(self) -> str:
        """Returns last seen value in text format."""
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
            print(e)
            return 'error'
        
    async def friend_list(self) -> (list | None):
        """Return a list of player's friends. NOTE: Return None if no friends found!"""
        friends_raw = self.data.get('friends', [])
        friends = [user['username'] for user in friends_raw]

        if not friends_raw:
            return None
        return friends
        
    async def friend_count(self):
        """Return number of friend(s). NOTE: Return None if no friends found!"""
        frineds = self.data.get('friends', [])
        if not frineds:
            return None
        return int(len(frineds))
        
    async def guild(self):
        """Fetch guild of the player.\n~~~\n\nreturn None if guild is not found:\n~~~"""
        if "clan" in self.data and self.data["clan"] is None:
            return None
            
        guild_data = self.data.get("clan", {})
        return GUILD(guild_data)