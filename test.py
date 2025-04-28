from buff import fetch_item_details

if __name__ == "__main__":
    url = "https://buff.163.com/goods/43091"
    item_name, wear_prices, style_prices = fetch_item_details(url)

    print(item_name)

    print("\n=== 磨损等级和价格 ===")
    for wear, price in wear_prices:
        print(f"{wear} ¥ {price}")

    print("\n=== 款式和价格 ===")
    for style, price in style_prices:
        print(f"{style} ¥ {price}")
