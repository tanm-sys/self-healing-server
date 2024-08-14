import psutil
import time
import aiohttp

async def check_cpu():
    return psutil.cpu_percent(interval=1)

async def check_memory():
    return psutil.virtual_memory().percent

async def check_disk():
    return psutil.disk_usage('/').percent

async def check_response_time(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()
            return time.time() - start_time

async def perform_health_checks(config):
    cpu_usage = await check_cpu()
    memory_usage = await check_memory()
    disk_usage = await check_disk()
    response_times = [await check_response_time(url) for url in config['server_urls']]
    avg_response_time = sum(response_times) / len(response_times)

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "response_time": avg_response_time
    }
