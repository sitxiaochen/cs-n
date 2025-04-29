# cs-n

本项目是一个用于爬取 BUFF.163 平台上 CS:GO 饰品价格信息、清洗数据并进行保存与可视化分析的工具。项目基于 Python 开发，模块化设计，既可独立运行也可供其他项目调用。

---

## 项目结构

```bash
cs-n/
├── buff/
│   ├── __init__.py
│   ├── fetch_buff_sp.py    # 抓取并解析 buff 页面商品数据
│   ├── test.py             # 测试 fetch_item_details 模块调用
│
├── venv/                   # 本地虚拟环境（不上传到 Git）
│
├── requirements.txt        # 项目依赖清单
├── README.md                # 项目说明文件
```

---

## 环境准备

1. 创建并激活虚拟环境（推荐）：

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

---

## 使用方法

### 方式一：作为独立脚本运行

运行 `buff/fetch_buff_sp.py`，自动爬取并打印饰品信息：

```bash
python buff/fetch_buff_sp.py
```

默认爬取 URL 可在文件中修改：

```python
url = "https://buff.163.com/goods/***"
fetch_item_details(url)
```

---

### 方式二：作为模块调用

在其他 Python 文件中导入并使用：

```python
from buff.fetch_buff_sp import fetch_item_details

url = "https://buff.163.com/goods/43091"
fetch_item_details(url)
```

---

## 示例输出

```
M9 刹刀（★） | 多普勒

=== 磨损等级和价格 ===
嵌新出厂 ¥ 15400
略有磨损 ¥ 15288
★ StatTrak™ ¥ 13333

=== 款式和价格 ===
不限款式 ¥ 15400
Phase1 ¥ 15400
Phase2 ¥ 29999
Phase3 ¥ 15450
Phase4 ¥ 18000
黑珍珠 ¥ 100000
红宝石 ¥ 111650
蓝宝石 ¥ 79000
```

---

## 依赖列表（requirements.txt）

```text
requests
beautifulsoup4
pandas
matplotlib
```

---

## 注意事项

- BUFF 平台部分数据是动态加载的，若后续遇到数据缺失情况，可使用 Selenium 或其他方案增强爬取能力。
- 频繁请求可能会被限制，建议适度增加随机延迟或配置代理。
- 项目目前以学习和数据分析为目的，非商业用途。

---

# 🚀 未来计划
- 支持更多平台（如 C5Game、IGXE）
- 增加价格变化趋势可视化
- 自动定时爬取与数据存档
- 异常价格预警系统

