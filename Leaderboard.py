from utils import *


class Sort:

    def __init__(self, data) -> None:
        self.data = data

    
    async def dict(self):
        """return's a dict"""

        pos = self.data["entries"]["place"]
        val = self.data["entries"]["value"]
        ply = self.data["entries"]["value"]

        