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


async def faulty(data: dict):

    """check faulty stats"""

    items = [
        (data["Bow kills"]),
        (data["Kills"]),
        (data["Games played"]),
        (data["Final deaths"]),
        (data["Arrows shot"]),
        (data["Highest winstreak reached"]),
        (data["Beds destroyed"]),
        (data["Losses"]),
        (data["Arrows hit"]),
        (data["Melee kills"]),
        (data["Final kills"]),
        (data["Deaths"]),
        (data["Void kills"]),
        (data["Wins"])
    ]

    for data_ in items:

        if (
            data_["metadata"] is None
            ) and (
                data_["entries"] is None
                ):
            
            #print(f'Error in response\n{data}')
            return True
    
    #print('Response is correct!')
    return False