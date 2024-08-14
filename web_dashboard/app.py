from flask import Flask, render_template, request
import sqlite3
import structlog

logger = structlog.get_logger()

app = Flask(__name__)
DATABASE = 'web_dashboard/health_data.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM health_data').fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
