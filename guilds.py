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

from datetime import datetime

class GUILD:
        
    """Wraps guild data"""
        
    def __init__(self, data):
        self.data = data

    async def name(self):
        """Returns guild name.\n~~~"""
        return self.data.get("name", None)
        
    async def tag(self):
        """Returns guild tag.\n~~~"""
        return self.data.get("tag", None)
        
    async def leader(self):
        """Returns username of the guild leader.\n~~~"""
        return self.data.get("owner", {}).get("username", None)
        
    async def level(self):
        """Returns current level of the guild.\n~~~"""
        return self.data.get("leveling",{}).get("level", None)
    
    async def exp(self):
        """Returns current exp of the guild."""
        return self.data.get("leveling",{}).get("exp", None)
    
    async def totalexp(self):
        """Returns current exp of the guild."""
        return self.data.get("leveling",{}).get("totalExp", None)
        
    async def member_list(self) -> list:
        """Returns guild members [LIST].\n~~~"""
        members = self.data.get("members", [])
        list = []
        for member in members:
            member_stats = member["user"]["username"]
            list.append(member_stats)
        return list 
        
    async def member_count(self) -> int:
        """Returns member count of the guild.\n~~~"""
        members = self.data.get("members", [])
        list = []
        for member in members:
            member_stats = member["user"]["username"]
            list.append(member_stats)
        return int(len(list))
    
    async def created_at(self):
        """Return timestamp of guild created at.\n~~~"""
        return f"{int(datetime.timestamp(datetime.fromisoformat(self.data.get('creationTime', 0))))}"
    
    async def raw(self):
        """Return data"""
        return self.data