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
from CraftiGames.utils import imports  # type: ignore
from CraftiGames.utils import (  # type: ignore
    interval,
    max_requests_per_interval as MAX_REQUESTS_PER_INTERVAL,
    delay
)

RATE_LIMIT_INTERVAL = imports.timedelta(seconds=interval)

last_request_time = imports.time.time()
API_requests = 0

async def avoid_rate_limits():
    """
    Handles rate limits for `PikaNetwork`'s API.
    """
    global API_requests, last_request_time

    current_time = imports.time.time()
    time_difference = current_time - last_request_time

    if time_difference > RATE_LIMIT_INTERVAL.total_seconds():
        API_requests = 0
        last_request_time = current_time

    API_requests += 1

    if API_requests > MAX_REQUESTS_PER_INTERVAL:
        imports.asyncio.create_task(log('Max request per interval reached: Delayed for: ', delay, ' sec'))
        await imports.asyncio.sleep(delay)
        API_requests = 0
        last_request_time = imports.time.time()