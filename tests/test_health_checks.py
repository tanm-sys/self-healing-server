import unittest
from health_checks import check_cpu, check_memory, check_disk, check_response_time

class TestHealthChecks(unittest.TestCase):

    async def test_check_cpu(self):
        cpu_usage = await check_cpu()
        self.assertIsNotNone(cpu_usage)
        self.assertGreaterEqual(cpu_usage, 0)
        self.assertLessEqual(cpu_usage, 100)

    async def test_check_memory(self):
        memory_usage = await check_memory()
        self.assertIsNotNone(memory_usage)
        self.assertGreaterEqual(memory_usage, 0)
        self.assertLessEqual(memory_usage, 100)

    async def test_check_disk(self):
        disk_usage = await check_disk()
        self.assertIsNotNone(disk_usage)
        self.assertGreaterEqual(disk_usage, 0)
        self.assertLessEqual(disk_usage, 100)

    async def test_check_response_time(self):
        response_time = await check_response_time('http://localhost:8000/health')
        self.assertIsNotNone(response_time)
        self.assertGreaterEqual(response_time, 0)

if __name__ == '__main__':
    unittest.main()
