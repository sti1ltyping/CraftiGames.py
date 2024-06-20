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


from CraftiGames._Logger import log  # type: ignore
from CraftiGames.utils import packages  # type: ignore
from CraftiGames.utils import config # type: ignore

delay = config.delay

last_request_time = packages.time.time()
API_requests = 0

async def avoid_rate_limits():
    """
    Handles rate limits for `JartexNetwork`'s API.
    """
    global API_requests, last_request_time

    current_time = packages.time.time()
    time_difference = current_time - last_request_time

    if time_difference > packages.timedelta(seconds=config.interval).total_seconds():
        API_requests = 0
        last_request_time = current_time

    API_requests += 1

    if API_requests > config.max_requests_per_interval:
        packages.asyncio.create_task(log('Max request per interval reached: Delayed for: ', delay, ' sec'))
        await packages.asyncio.sleep(delay)
        API_requests = 0
        last_request_time = packages.time.time()