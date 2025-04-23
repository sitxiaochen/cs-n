import sqlite3
import matplotlib.pyplot as plt
from config import DB_PATH

def get_latest_data(limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT name, sell_min_price, sell_num, timestamp
        FROM csgo_items
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    data = c.fetchall()
    conn.close()
    return data

def plot_price_and_volume():
    data = get_latest_data()

    if not data:
        print("无数据可视化")
        return

    names = [row[0] for row in data]
    prices = [row[1] for row in data]
    volumes = [row[2] for row in data]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.barh(names, prices, color='skyblue')
    plt.title("饰品价格")
    plt.xlabel("价格 (¥)")
    plt.tight_layout()

    plt.subplot(1, 2, 2)
    plt.barh(names, volumes, color='orange')
    plt.title("在售数量")
    plt.xlabel("数量")
    plt.tight_layout()

    plt.show()

# 示例
if __name__ == "__main__":
    plot_price_and_volume()
