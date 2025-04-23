import asyncio
from csgo_price_scraper import fetch_item_prices  # 爬取数据
from data_visualizer import plot_item_prices  # 可视化数据
from exporter import export_to_csv, export_to_excel  # 数据导出
from anomaly_detector import detect_anomalies  # 异常检测

async def main():
    # 1. 爬取数据并存储
    print("正在爬取数据...")
    await fetch_item_prices()

    # 2. 可视化数据
    print("正在生成价格图表...")
    plot_item_prices()

    # 3. 执行异常检测
    print("正在检测异常价格...")
    detect_anomalies()

    # 4. 导出数据到文件
    print("正在导出数据...")
    export_to_csv()  # 或者 export_to_excel()

if __name__ == "__main__":
    # 启动主程序
    asyncio.run(main())
