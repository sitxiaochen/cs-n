import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS csgo_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sell_min_price REAL,
        sell_num INTEGER,
        buy_num INTEGER,
        goods_id TEXT,
        img_url TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def insert_items(items):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for item in items:
        c.execute("""
        INSERT INTO csgo_items (name, sell_min_price, sell_num, buy_num, goods_id, img_url)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item["name"], item["sell_min_price"], item["sell_num"],
            item["buy_num"], item["goods_id"], item["img_url"]
        ))
    conn.commit()
    conn.close()

# 示例用法
if __name__ == "__main__":
    from data_parser import parse_buff_items
    from data_fetcher import fetch_multiple_pages
    import asyncio

    async def test():
        init_db()
        raw = await fetch_multiple_pages(1)
        items = parse_buff_items(raw[0])
        insert_items(items)
        print("数据已写入数据库。")

    asyncio.run(test())
