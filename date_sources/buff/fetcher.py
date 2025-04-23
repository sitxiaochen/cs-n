import aiohttp
import asyncio
from config import BUFF_API_URL, HEADERS, DEFAULT_PARAMS

async def fetch_buff_data(session, params):
    try:
        async with session.get(BUFF_API_URL, headers=HEADERS, params=params) as response:
            return await response.json()
    except Exception as e:
        print(f"请求失败: {e}")
        return None

async def fetch_multiple_pages(page_range=3):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(1, page_range + 1):
            params = DEFAULT_PARAMS.copy()
            params["page_num"] = page
            tasks.append(fetch_buff_data(session, params))
        return await asyncio.gather(*tasks)

# 测试入口
if __name__ == "__main__":
    data = asyncio.run(fetch_multiple_pages(2))
    print(data[0])  # 打印第一页数据
