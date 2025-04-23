from flask import Flask, render_template
import sqlite3
from config import DB_PATH

app = Flask(__name__)

def get_items():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, sell_min_price, sell_num FROM csgo_items ORDER BY timestamp DESC LIMIT 10")
    items = c.fetchall()
    conn.close()
    return items

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
