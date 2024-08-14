import aiohttp
import asyncio
import structlog

logger = structlog.get_logger()

async def monitor_servers(server_urls):
    async with aiohttp.ClientSession() as session:
        for url in server_urls:
            try:
                async with session.get(url) as response:
                    logger.info(f"Monitored {url} with status {response.status}")
            except Exception as e:
                logger.error(f"Failed to monitor {url}", error=str(e))
