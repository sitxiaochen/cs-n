import sqlite3
import csv
import pandas as pd
from config import DB_PATH

def export_to_csv(file_path='csgo_items.csv'):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 获取所有数据
    c.execute("SELECT * FROM csgo_items")
    rows = c.fetchall()

    # 获取列名
    column_names = [description[0] for description in c.description]

    # 写入 CSV 文件
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # 写入列名
        writer.writerows(rows)         # 写入数据

    conn.close()
    print(f"数据已导出至 {file_path}")

def export_to_excel(file_path='csgo_items.xlsx'):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 获取所有数据
    c.execute("SELECT * FROM csgo_items")
    rows = c.fetchall()

    # 获取列名
    column_names = [description[0] for description in c.description]

    # 使用 pandas 导出到 Excel
    df = pd.DataFrame(rows, columns=column_names)
    df.to_excel(file_path, index=False)

    conn.close()
    print(f"数据已导出至 {file_path}")

# 示例
if __name__ == "__main__":
    export_to_csv()  # 导出为 CSV
    export_to_excel()  # 导出为 Excel
