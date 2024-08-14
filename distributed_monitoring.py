import aiohttp
import asyncio

class DistributedMonitoring:
    def __init__(self, server_urls):
        self.server_urls = server_urls

    async def collect_data(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_health_data(session, url) for url in self.server_urls]
            results = await asyncio.gather(*tasks)
            return results

    async def fetch_health_data(self, session, url):
        async with session.get(url) as response:
            return await response.json()
