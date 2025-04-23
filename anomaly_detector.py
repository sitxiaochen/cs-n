import sqlite3
from config import DB_PATH

def detect_price_anomalies(threshold_percent=30):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 查询每个饰品最近两次记录
    c.execute("""
        SELECT name, sell_min_price, timestamp
        FROM (
            SELECT *
            FROM csgo_items
            ORDER BY timestamp DESC
        )
        GROUP BY name
    """)
    latest_prices = c.fetchall()

    anomalies = []

    for name, latest_price, timestamp in latest_prices:
        c.execute("""
            SELECT sell_min_price FROM csgo_items
            WHERE name = ?
            ORDER BY timestamp DESC
            LIMIT 2
        """, (name,))
        rows = c.fetchall()
        if len(rows) == 2:
            new_price, old_price = rows[0][0], rows[1][0]
            change = ((new_price - old_price) / old_price) * 100 if old_price else 0
            if abs(change) >= threshold_percent:
                anomalies.append((name, old_price, new_price, round(change, 2)))

    conn.close()
    return anomalies

# 示例
if __name__ == "__main__":
    results = detect_price_anomalies()
    for r in results:
        print(f"⚠️ {r[0]}: {r[1]} -> {r[2]} ({r[3]}%)")
