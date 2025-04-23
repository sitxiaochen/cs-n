def parse_buff_items(json_data):
    """
    解析 buff 返回的 JSON 数据，提取饰品信息列表
    """
    if not json_data or "data" not in json_data:
        return []

    items = json_data["data"].get("items", [])
    parsed = []

    for item in items:
        parsed.append({
            "name": item.get("name"),
            "sell_min_price": float(item.get("sell_min_price", 0)),
            "sell_num": int(item.get("sell_num", 0)),
            "buy_num": int(item.get("buy_num", 0)),
            "goods_id": item.get("id"),
            "img_url": item.get("goods_info", {}).get("icon_url"),
        })

    return parsed

# 示例用法
if __name__ == "__main__":
    from data_fetcher import fetch_multiple_pages
    import asyncio

    async def test():
        raw_data_list = await fetch_multiple_pages(1)
        for raw in raw_data_list:
            parsed = parse_buff_items(raw)
            for item in parsed[:3]:
                print(item)

    asyncio.run(test())
