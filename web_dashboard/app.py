from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('data/health_data.db')  # Adjusted to correct path
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM health_data ORDER BY timestamp DESC LIMIT 10')
    data = cursor.fetchall()
    return render_template('dashboard.html', data=data)

if __name__ == "__main__":
    app.run(port=5000)
