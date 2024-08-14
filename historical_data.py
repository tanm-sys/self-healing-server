import sqlite3

class HistoricalData:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS health_data (
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL,
            response_time REAL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def store_data(self, health_data):
        query = '''
        INSERT INTO health_data (cpu_usage, memory_usage, disk_usage, response_time)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (health_data['cpu_usage'], health_data['memory_usage'], health_data['disk_usage'], health_data['response_time']))
        self.conn.commit()
