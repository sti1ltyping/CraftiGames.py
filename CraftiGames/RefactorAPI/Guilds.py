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

from CraftiGames.utils import imports, UnixTimestamp # type: ignore

class Guild:
    """
    Wraps guild API
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
    SOFTWARE.
    """
        
    def __init__(self, data):
        self.raw: dict = data

    @property
    def name(self) -> str:
        """
        Returns:
        - Guild's name.
        """
        return self.raw.get("name", '')
        
    @property
    def tag(self) -> str:
        """
        Returns:
        - Guild's tag.
        """
        return self.raw.get("tag", '')
        
    @property
    def leader(self) -> str:
        """
        Returns:
        - Guild's leader's username.
        """
        return self.raw.get("owner", {}).get("username", '')

    @property
    def link(self) -> str:
        """
        Returns:
        - PikaNetwork link to the leader's profile.
        """
        return f"https://stats.pika-network.net/player/{self.leader}"
        
    @property
    def level(self) -> int:
        """
        Returns:
        - Guild's level.
        """
        return int(self.raw.get("leveling",{}).get("level", 0))
    
    @property
    def exp(self) -> int:
        """
        Returns:
        - Guild's exp.
        """
        return int(self.raw.get("leveling",{}).get("exp", 0))
    
    @property
    def totalexp(self) -> int:
        """
        Returns:
        - Guild's total exp.
        """
        return int(self.raw.get("leveling",{}).get("totalExp", 0))
        
    @property
    def member_list(self) -> list:
        """
        Returns:
        - Guild member's list.
        """    
        return [username["user"]["username"] for username in self.raw.get("members", [])]
        
    @property
    def member_count(self) -> int:
        """
        Returns:
        - Member count of the guild.
        """
        return len(self.member_list)
    
    @property
    def created_at(self) -> UnixTimestamp:
        """
        Returns:
        - UnixTimestamp (usable in discord timestamp) of guild's creation date-time.
        """
        return int(imports.datetime.timestamp(imports.datetime.fromisoformat(self.raw.get('creationTime', 0))))
    

class Clan:
    """
    Wraps Clan API
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
    SOFTWARE.
    """
        
    def __init__(self, data):
        self.raw: dict = data

    @property
    def name(self) -> str:
        """
        Returns:
        - Clan's name.
        """
        return self.raw.get("name", '')
        
    @property
    def tag(self) -> str:
        """
        Returns:
        - Clan's tag.
        """
        return self.raw.get("tag", '')
    
    @property
    def currentTrophies(self) -> int:
        """
        Returns:
        - Clan's current trophies.
        """
        return int(self.raw.get("currentTrophies", 0))
    
    @property
    def owner(self) -> str:
        """
        Returns:
        - Clan's owner's username.
        """
        return self.raw.get("owner", {}).get("username", '')

    @property
    def link(self) -> str:
        """
        Returns:
        - PikaNetwork link to the leader's profile.
        """
        return f"https://stats.jartexnetwork.com/player/{self.owner}"
        
    @property
    def level(self) -> int:
        """
        Returns:
        - Clan's level.
        """
        return int(self.raw.get("leveling",{}).get("level", 0))
    
    @property
    def exp(self) -> int:
        """
        Returns:
        - Clan's exp.
        """
        return int(self.raw.get("leveling",{}).get("exp", 0))
    
    @property
    def totalexp(self) -> int:
        """
        Returns:
        - Clan's total exp.
        """
        return int(self.raw.get("leveling",{}).get("totalExp", 0))
        
    @property
    def member_list(self) -> list:
        """
        Returns:
        - Clan member's list.
        """    
        return [username["user"]["username"] for username in self.raw.get("members", [])]
        
    @property
    def member_count(self) -> int:
        """
        Returns:
        - Clan count of the guild.
        """
        return len(self.member_list)
    
    @property
    def created_at(self) -> UnixTimestamp:
        """
        Returns:
        - UnixTimestamp (usable in discord timestamp) of Clan's creation date-time.
        """
        return int(imports.datetime.timestamp(imports.datetime.fromisoformat(self.raw.get('creationTime', 0))))