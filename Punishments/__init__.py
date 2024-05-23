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


class History:
    """
    Wraps Punishment History
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

    def __init__(self, html_) -> None:
        self.__html_parser__: str = html_


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
            punishement_type: imports.Literal["all", "ban", "warn", "kick", "mute"] = "all"
            ) -> dict:

        soup = imports.BeautifulSoup(self.__html_parser__, 'html.parser')
        player = soup.title.string[:-28] if soup.title is not None else "Not found"
        punishments: dict = {}
        prow = []
        for row in soup.find_all(class_='row'):
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

            prow.append(
                {
                    "Reason": reason,
                    "Date": date,
                    "Expires": expires,
                    "Type": ptype,
                    "By": by
                }
            )
        punishments[player] = prow

        return punishments