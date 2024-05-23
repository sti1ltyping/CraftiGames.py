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

from PikaPY.utils import imports # type: ignore

class Guild:
    """
    Wraps guild API
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
    SOFTWARE.
    """
        
    def __init__(self, data):
        self.data: dict = data

    async def name(self) -> str:
        """
        Returns:
        - Guild's name.
        """
        return self.data.get("name", None)
        
    async def tag(self) -> str:
        """
        Returns:
        - Guild's tag.
        """
        return self.data.get("tag", None)
        
    async def leader(self) -> str:
        """
        Returns:
        - Guild's leader's username.
        """
        return self.data.get("owner", {}).get("username", None)
        
    async def level(self) -> int:
        """
        Returns:
        - Guild's level.
        """
        return int(self.data.get("leveling",{}).get("level", 0))
    
    async def exp(self) -> int:
        """
        Returns:
        - Guild's exp.
        """
        return int(self.data.get("leveling",{}).get("exp", 0))
    
    async def totalexp(self) -> int:
        """
        Returns:
        - Guild's total exp.
        """
        return int(self.data.get("leveling",{}).get("totalExp", 0))
        
    async def member_list(self) -> list:
        """
        Returns:
        - Guild member's list.
        """    
        return [username["user"]["username"] for username in self.data.get("members", [])]
        
    async def member_count(self) -> int:
        """
        Returns:
        - Member count of the guild.
        """
        return len(await self.member_list())
    
    async def created_at(self) -> int:
        """
        Returns:
        - Discord timestamp int of guild's creation date.
        """
        return int(imports.datetime.timestamp(imports.datetime.fromisoformat(self.data.get('creationTime', 0))))
    
    async def raw(self) -> dict:
        """
        Returns:
        - Raw data.
        """
        return self.data