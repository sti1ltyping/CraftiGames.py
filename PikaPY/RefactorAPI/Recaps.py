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

from PikaPY.utils import imports, UnixTimestamp

class player: ...
class value: ...

class TopPlayers:
    """
    Leaderboard (helper class)
    ~~~~~~~~

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
    
    def __init__(self, users: list[dict[str, dict[str, int]]]) -> None:
        self.users = users
        self.leaderboard = self.calculate_leaderboard()
    
    def calculate_leaderboard(self) -> dict[str, list[dict[str, int]]]:
        stats_leaderboard = {
            "time_of_death_ms": [],
            "blocks_moved": [],
            "items_bought": [],
            "resources_collected": [],
            "deaths": [],
            "blocks_placed": [],
            "assists": [],
            "final_kills": [],
            "blocks_mined": [],
            "kills": [],
            "beds_destroyed": []
        }
        
        for user in self.users:
            username = user.get("username", '')
            stats = user.get("stats", {})

            time_of_death_ms = int(stats.get("Time of death (ms)", 0))
            blocks_moved = int(stats.get("Blocks moved", 0))
            items_bought = int(stats.get("Items bought", 0))
            resources_collected = int(stats.get("Resources collected", 0))
            deaths = int(stats.get("Deaths", 0))
            blocks_placed = int(stats.get("Blocks placed", 0))
            assists = int(stats.get("Assists", 0))
            final_kills = int(stats.get("Final kills", 0))
            blocks_mined = int(stats.get("Blocks mined", 0))
            kills = int(stats.get("Kills", 0))
            beds_destroyed = int(stats.get("Beds destroyed", 0))

            stats_leaderboard["time_of_death_ms"].append({"player": username, "value": time_of_death_ms})
            stats_leaderboard["blocks_moved"].append({"player": username, "value": blocks_moved})
            stats_leaderboard["items_bought"].append({"player": username, "value": items_bought})
            stats_leaderboard["resources_collected"].append({"player": username, "value": resources_collected})
            stats_leaderboard["deaths"].append({"player": username, "value": deaths})
            stats_leaderboard["blocks_placed"].append({"player": username, "value": blocks_placed})
            stats_leaderboard["assists"].append({"player": username, "value": assists})
            stats_leaderboard["final_kills"].append({"player": username, "value": final_kills})
            stats_leaderboard["blocks_mined"].append({"player": username, "value": blocks_mined})
            stats_leaderboard["kills"].append({"player": username, "value": kills})
            stats_leaderboard["beds_destroyed"].append({"player": username, "value": beds_destroyed})
        
        for stat in stats_leaderboard:
            stats_leaderboard[stat] = sorted(stats_leaderboard[stat], key=lambda x: x["value"], reverse=True)
        
        return stats_leaderboard


class Recap:
    """
    Wrap Recap
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

    def __init__(self, data: dict):
        self.raw: dict = data
        self.top_players = TopPlayers(
            self.raw.get(
                "users", []
            )
        )

    @property
    def id(self) -> str:
        """
        Returns:
        - ID of the recap.
        """
        return self.raw.get("id", '')
    
    @property
    def link(self) -> str:
        """
        Returns:
        - PikaNetwork link to the recap.
        """
        return f"https://stats.pika-network.net/recap/{self.id}"
    
    @property
    def map_name(self) -> str:
        """
        Returns:
        - Name of the map.
        """
        return self.raw.get("mapName", '')
    
    @property
    def game_type(self) -> str:
        """
        Returns:
        - Gamemode of the recap i.e. 'bedwars', 'skywars,...
        """
        return self.raw.get("gameType", '')
    
    @property
    def game_server_name(self) -> str:
        """
        Returns:
        - Game server name.
        """
        return self.raw.get("gameServerName", '')
    
    @property
    def game_start(self) -> int:
        """
        Returns:
        - Unix timestamp (usable in Discord timestamp) of game's starting date-time.
        """
        iso_format = self.raw.get("gameStart", None)
        if iso_format:
            try:
                dt = imports.datetime.fromisoformat(iso_format.replace("Z", "+00:00"))
                return int(dt.timestamp())
            except ValueError as e:
                return 0
        return 0
    
    @property
    def game_duration(self) -> str:
        """
        Returns:
        - Duration of game.
        """
        return self.raw.get("gameDuration", '')
    
    @property
    def players(self) -> list[str]:
        """
        Returns:
        - List of all players in the match.
        """
        _players = self.raw.get("users", [])
        return [player["username"] for player in _players] if _players else []
    
    @property
    def player_count(self) -> int:
        """
        Returns:
        - Number of players in the game.
        """
        return len(self.players)

    @property
    def winners(self) -> list[str]:
        """
        Returns:
        - List of the winners.
        """
        return self.raw.get("winners", [])
    
    @property
    def most_kills(self) -> int:
        """
        Returns:
        - Value of most kills in the game.
        """
        return self.top_players.leaderboard["kills"][0]["value"] if self.top_players.leaderboard["kills"] else 0
    
    @property
    def player_with_most_kills(self) -> str:
        """
        Returns:
        - Username of the player who has most kills.
        """
        return self.top_players.leaderboard["kills"][0]["player"] if self.top_players.leaderboard["kills"] else ""
    
    @property
    def most_deaths(self) -> int:
        """
        Returns:
        - Value of most deaths in the game.
        """
        return self.top_players.leaderboard["deaths"][0]["value"] if self.top_players.leaderboard["deaths"] else 0
    
    @property
    def player_with_most_deaths(self) -> str:
        """
        Returns:
        - Username of the player who has most deaths.
        """
        return self.top_players.leaderboard["deaths"][0]["player"] if self.top_players.leaderboard["deaths"] else ""

    @property
    def last_death_time_ms(self) -> int:
        """
        Returns:
        - Time (ms) when last player was killed.
        """
        return self.top_players.leaderboard["time_of_death_ms"][0]["value"] if self.top_players.leaderboard["time_of_death_ms"] else 0

    @property
    def last_player_to_die(self) -> str:
        """
        Returns:
        - Username of the last player to get killed.
        """
        return self.top_players.leaderboard["time_of_death_ms"][0]["player"] if self.top_players.leaderboard["time_of_death_ms"] else ""

    @property
    def most_blocks_moved(self) -> int:
        """
        Returns:
        - Value of most blocks moved in the game.
        """
        return self.top_players.leaderboard["blocks_moved"][0]["value"] if self.top_players.leaderboard["blocks_moved"] else 0

    @property
    def player_with_most_blocks_moved(self) -> str:
        """
        Returns:
        - Username of the player who has moved most blocks.
        """
        return self.top_players.leaderboard["blocks_moved"][0]["player"] if self.top_players.leaderboard["blocks_moved"] else ""

    @property
    def most_items_bought(self) -> int:
        """
        Returns:
        - Value of most items bought in the game.
        """
        return self.top_players.leaderboard["items_bought"][0]["value"] if self.top_players.leaderboard["items_bought"] else 0

    @property
    def player_with_most_items_bought(self) -> str:
        """
        Returns:
        - Username of the player who has bought most item.
        """
        return self.top_players.leaderboard["items_bought"][0]["player"] if self.top_players.leaderboard["items_bought"] else ""

    @property
    def most_resources_collected(self) -> int:
        """
        Returns:
        - Value of most resources collected in the game.
        """
        return self.top_players.leaderboard["resources_collected"][0]["value"] if self.top_players.leaderboard["resources_collected"] else 0

    @property
    def player_with_most_resources_collected(self) -> str:
        """
        Returns:
        - Username of the player who has collected most resources.
        """
        return self.top_players.leaderboard["resources_collected"][0]["player"] if self.top_players.leaderboard["resources_collected"] else ""

    @property
    def most_blocks_placed(self) -> int:
        """
        Returns:
        - Value of most blocks placed in the game.
        """
        return self.top_players.leaderboard["blocks_placed"][0]["value"] if self.top_players.leaderboard["blocks_placed"] else 0

    @property
    def player_with_most_blocks_placed(self) -> str:
        """
        Returns:
        - Username of the player who has placed most blocks.
        """
        return self.top_players.leaderboard["blocks_placed"][0]["player"] if self.top_players.leaderboard["blocks_placed"] else ""

    @property
    def most_assists(self) -> int:
        """
        Returns:
        - Value of most assists in the game.
        """
        return self.top_players.leaderboard["assists"][0]["value"] if self.top_players.leaderboard["assists"] else 0

    @property
    def player_with_most_assists(self) -> str:
        """
        Returns:
        - Username of the player who has assisted the most.
        """
        return self.top_players.leaderboard["assists"][0]["player"] if self.top_players.leaderboard["assists"] else ""

    @property
    def most_final_kills(self) -> int:
        """
        Returns:
        - Value of most final kills in the game.
        """
        return self.top_players.leaderboard["final_kills"][0]["value"] if self.top_players.leaderboard["final_kills"] else 0

    @property
    def player_with_most_final_kills(self) -> str:
        """
        Returns:
        - Username of the player who has most final kills.
        """
        return self.top_players.leaderboard["final_kills"][0]["player"] if self.top_players.leaderboard["final_kills"] else ""

    @property
    def most_blocks_mined(self) -> int:
        """
        Returns:
        - Value of most block mined in the game.
        """
        return self.top_players.leaderboard["blocks_mined"][0]["value"] if self.top_players.leaderboard["blocks_mined"] else 0

    @property
    def player_with_most_blocks_mined(self) -> str:
        """
        Returns:
        - Username of the player who has mined most blocks.
        """
        return self.top_players.leaderboard["blocks_mined"][0]["player"] if self.top_players.leaderboard["blocks_mined"] else ""

    @property
    def most_beds_destroyed(self) -> int:
        """
        Returns:
        - Value of most beds destroyed in the game.
        """
        return self.top_players.leaderboard["beds_destroyed"][0]["value"] if self.top_players.leaderboard["beds_destroyed"] else 0

    @property
    def player_with_most_beds_destroyed(self) -> str:
        """
        Returns:
        - Username of the player who has destroyed most beds.
        """
        return self.top_players.leaderboard["beds_destroyed"][0]["player"] if self.top_players.leaderboard["beds_destroyed"] else ""
    
    @property
    def leaderboard_time_of_death(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: time of death (ms).
        
        Returns:
        - A list of player and time of death sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 11142},
            {"player": "player_2", "value": 10523},
            {"player": "player_3", "value": 8523}
        ]
        ```
        """
        return self.top_players.leaderboard["time_of_death_ms"]
    
    @property
    def leaderboard_blocks_moved(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of blocks.
        
        Returns:
        - A list of player and number of blocks moved sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 53},
            {"player": "player_2", "value": 32},
            {"player": "player_3", "value": 20}
        ]
        ```
        """
        return self.top_players.leaderboard["blocks_moved"]
    
    @property
    def leaderboard_items_bought(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: items bought.
        
        Returns:
        - A list of player and number items bought moved sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 53},
            {"player": "player_2", "value": 32},
            {"player": "player_3", "value": 20}
        ]
        ```
        """
        return self.top_players.leaderboard["items_bought"]
    
    @property
    def leaderboard_resources_collected(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of resources collected.
        
        Returns:
        - A list of player and number of resources collected sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 53},
            {"player": "player_2", "value": 32},
            {"player": "player_3", "value": 20}
        ]
        ```
        """
        return self.top_players.leaderboard["resources_collected"]
    
    @property
    def leaderboard_deaths(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of deaths.
        
        Returns:
        - A list of player and number of deaths sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 8},
            {"player": "player_2", "value": 4},
            {"player": "player_3", "value": 2}
        ]
        ```
        """
        return self.top_players.leaderboard["deaths"]
    
    @property
    def leaderboard_blocks_placed(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of blocks placed.
        
        Returns:
        - A list of player and number of blocks placed sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 623},
            {"player": "player_2", "value": 332},
            {"player": "player_3", "value": 220}
        ]
        ```
        """
        return self.top_players.leaderboard["blocks_placed"]
    
    @property
    def leaderboard_assists(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of assists.
        
        Returns:
        - A list of player and number of assists sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 5},
            {"player": "player_2", "value": 2},
            {"player": "player_3", "value": 1}
        ]
        ```
        """
        return self.top_players.leaderboard["assists"]
    
    @property
    def leaderboard_final_kills(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of final kills.
        
        Returns:
        - A list of player and number of final kills sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 3},
            {"player": "player_2", "value": 2},
            {"player": "player_3", "value": 0}
        ]
        ```
        """
        return self.top_players.leaderboard["final_kills"]
    
    @property
    def leaderboard_blocks_mined(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of blocks mined.
        
        Returns:
        - A list of player and number of blocks mined sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 23},
            {"player": "player_2", "value": 32},
            {"player": "player_3", "value": 20}
        ]
        ```
        """
        return self.top_players.leaderboard["blocks_mined"]
    
    @property
    def leaderboard_kills(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of kills.
        
        Returns:
        - A list of player and number of kills sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 10},
            {"player": "player_2", "value": 5},
            {"player": "player_3", "value": 2}
        ]
        ```
        """
        return self.top_players.leaderboard["kills"]
    
    @property
    def leaderboard_beds_destroyed(self) -> list[dict[player, value]]:
        """
        Keys:
        - `player`: username of the player.
        - `value`: number of beds destroyed.
        
        Returns:
        - A list of player and number of beds destroyed sorted highest to lowest.

        Example:
        ```json
        [
            {"player": "player_1", "value": 5},
            {"player": "player_2", "value": 3},
            {"player": "player_3", "value": 0}
        ]
        ```
        """
        return self.top_players.leaderboard["beds_destroyed"]