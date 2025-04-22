import aiohttp
import asyncio
import csv
from datetime import datetime

STEAM_API_URL = "https://steamcommunity.com/market/priceoverview/"

# 示例饰品（Steam市场完整名）
sample_item = "AK-47 | Redline (Field-Tested)"

# 参数拼接函数
def build_url(item_name):
    return f"{STEAM_API_URL}?currency=23&appid=730&market_hash_name={item_name.replace(' ', '%20')}"

# 主函数：获取数据
async def fetch_steam_price(item_name):
    url = build_url(item_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
            data = await response.json()
            return {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "steam",
                "item_name": item_name,
                "lowest_price": data.get("lowest_price", ""),
                "median_price": data.get("median_price", ""),
                "volume": data.get("volume", "")
            }

# 保存数据到 CSV
def save_to_csv(data, filename="steam_prices.csv"):
    file_exists = False
    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# 异步入口
async def main():
    item_data = await fetch_steam_price(sample_item)
    save_to_csv(item_data)
    print("✅ 数据已写入:", item_data)

# 运行
if __name__ == "__main__":
    asyncio.run(main())
