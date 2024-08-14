import aiohttp
import asyncio
import logging
import json

async def fetch_health_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def monitor_servers(server_urls):
    while True:
        tasks = [fetch_health_status(url) for url in server_urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            if result['status'] != 'healthy':
                logging.warning("Unhealthy server detected: %s", result)
        await asyncio.sleep(60)

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)
      
