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
from typing import Literal

class History:

    def __init__(self, html_) -> None:
        self.html_parser: str = html_
        self.punishments: dict = {}


    async def bans(
            self,
            list_console: bool = True
            ) -> dict:
        return await self.all(list_console, "ban")
    
    async def warns(
            self,
            list_console: bool = True
            ) -> dict:
        return await self.all(list_console, "warn")
    
    async def kicks(
            self,
            list_console: bool = True
            ) -> dict:
        return await self.all(list_console, "kick")
    
    async def mutes(
            self,
            list_console: bool = True
            ) -> dict:
        return await self.all(list_console, "mute")

    async def all(
            self, 
            list_console: bool = True,
            punishement_type: Literal["all", "ban", "warn", "kick", "mute"] = "all"
            ) -> dict:

        self.soup = imports.BeautifulSoup(self.html_parser, 'html.parser')
        self.player = self.soup.title.string[:-28] if self.soup.title is not None else "Not found"
        self.punishments.clear()
        self.prow = []
        for row in self.soup.find_all(class_='row'):
            row: imports.BeautifulSoup

            reason = row.find(class_='_reason').text.strip()
            date = row.find(class_='_date').text.strip()
            expires = row.find(class_='_expires').text.strip()
            ptype = row.find(class_='_type').find('b').text.strip()
            by = row.find(class_='user-link').text.strip()
            
            if list_console is False and by.lower() == 'console':
                continue
            
            if punishement_type.lower() != 'all' and ptype.lower() != punishement_type.lower():
                continue

            self.prow.append(
                {
                    "Reason": reason,
                    "Date": date,
                    "Expires": expires,
                    "Type": ptype,
                    "By": by
                }
            )
        self.punishments[self.player] = self.prow

        return self.punishments


    async def main(self):
        list_console = input("List Console? [yes/no]: ")
        ban_type = input("Type: [all, ban, warn, kick, mute]: ")
        await self.scrape_website(list_console, ban_type)