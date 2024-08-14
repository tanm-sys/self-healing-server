import psutil
import aiohttp
import asyncio
import logging
import structlog

logger = structlog.get_logger()

async def check_cpu():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        logger.error("Failed to check CPU usage", error=str(e))
        return None

async def check_memory():
    try:
        memory = psutil.virtual_memory()
        return memory.percent
    except Exception as e:
        logger.error("Failed to check memory usage", error=str(e))
        return None

async def check_disk():
    try:
        disk = psutil.disk_usage('/')
        return disk.percent
    except Exception as e:
        logger.error("Failed to check disk usage", error=str(e))
        return None

async def check_response_time(url):
    try:
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await response.text()
                return time.time() - start_time
    except aiohttp.ClientError as e:
        logger.error(f"Failed to fetch {url}", error=str(e))
        return float('inf')

async def check_health(server_urls):
    results = []
    for url in server_urls:
        cpu = await check_cpu()
        memory = await check_memory()
        disk = await check_disk()
        response_time = await check_response_time(url)
        results.append((cpu, memory, disk, response_time))
    return results
