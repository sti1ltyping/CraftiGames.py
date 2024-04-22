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


import time
from datetime import timedelta
import asyncio
import json


with open('PikaPY/Ratelimits/Settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

    Interval: int = settings['Ratelimit']['Interval']
    MAX_REQUESTS_PER_INTERVAL: int = settings['Ratelimit']['Request Per Interval']

    delay: float = settings['Ratelimit']['Delay']


RATE_LIMIT_INTERVAL = timedelta(seconds=Interval)

last_request_time = time.time()
API_requests = 0


async def avoid_rate_limits():
    """
    Handles rate limits
    """
    global API_requests, last_request_time

    API_requests += 1

    current_time = time.time()
    time_difference = current_time - last_request_time

    #print(f'sent API request, count: {API_requests}')
    if API_requests >= MAX_REQUESTS_PER_INTERVAL and time_difference <= RATE_LIMIT_INTERVAL.total_seconds():
        #print(f'MAX REQUESTS PER INTERVAL REACHED: Delayed for {delay}')
        await asyncio.sleep(delay)

        API_requests, last_request_time = 0, time.time()

    last_request_time = current_time