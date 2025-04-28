import requests
from bs4 import BeautifulSoup
import copy

def fetch_item_details(url):
    """给定商品url，返回商品信息（名称，磨损等级价格列表，款式价格列表）"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"无法访问页面，状态码: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    # 商品名称
    item_name_tag = soup.find("h1")
    if item_name_tag:
        item_name = item_name_tag.text.strip()
        item_name = item_name.split(" (")[0]
    else:
        raise Exception("未找到商品名称")

    # 磨损等级和价格
    scope_btns = soup.find("div", class_="scope-btns")
    wear_prices = []
    if scope_btns:
        pending_text = None
        for elem in scope_btns.children:
            if elem.name == "a":
                temp_a = copy.copy(elem)
                for bad in temp_a.find_all(["span", "i"]):
                    bad.decompose()
                text = temp_a.get_text(strip=True)
                price_tag = elem.find("span", class_="custom-currency")
                if price_tag:
                    price = price_tag.get("data-price", "").strip()
                    wear_prices.append((text, price))
            elif elem.string and elem.string.strip():
                pending_text = elem.string.strip()
            elif elem.name == "span" and elem.get("class") == ["custom-currency"]:
                if pending_text:
                    price = elem.get("data-price", "").strip()
                    wear_prices.append((pending_text, price))
                    pending_text = None

    # 款式和价格
    j_fav = soup.find("div", id="j_fav")
    style_prices = []
    if j_fav:
        seen = set()
        for li in j_fav.find_all("li"):
            style = li.get("title", "").strip()
            price_tag = li.find("span", class_="custom-currency")
            if style and price_tag:
                price = price_tag.get("data-price", "").strip()
                if (style, price) not in seen:
                    seen.add((style, price))
                    style_prices.append((style, price))

    return item_name, wear_prices, style_prices
