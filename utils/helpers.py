import logging
import time
import json
import re
from datetime import datetime
from typing import Any, Callable


# 设置日志
def setup_logging(log_file: str = 'app.log'):
    """
    设置日志记录器，用于日志文件和控制台输出
    :param log_file: 日志文件名
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # 输出到控制台
            logging.FileHandler(log_file)  # 输出到文件
        ]
    )
    logging.info("日志设置完成")


# 重试机制
def retry(func: Callable, retries: int = 3, delay: int = 2, *args, **kwargs) -> Any:
    """
    封装一个带重试的函数
    :param func: 需要重试的函数
    :param retries: 最大重试次数
    :param delay: 每次重试的延迟（秒）
    :param args: 传递给func的参数
    :param kwargs: 传递给func的关键字参数
    :return: 函数返回值
    """
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                logging.error(f"All {retries} attempts failed.")
                raise


# 格式转换：日期字符串转 datetime 对象
def parse_date(date_string: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    将日期字符串转换为 datetime 对象
    :param date_string: 日期字符串
    :param date_format: 日期格式
    :return: datetime 对象
    """
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        logging.error(f"日期转换失败: {e}")
        raise


# 格式转换：JSON 转 Python 字典
def json_to_dict(json_string: str) -> dict:
    """
    将 JSON 字符串转换为字典
    :param json_string: JSON 格式字符串
    :return: 字典
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logging.error(f"JSON解析失败: {e}")
        raise


# 格式转换：Python 字典转 JSON
def dict_to_json(data: dict) -> str:
    """
    将字典转换为 JSON 字符串
    :param data: 字典
    :return: JSON 字符串
    """
    try:
        return json.dumps(data, indent=4)
    except (TypeError, ValueError) as e:
        logging.error(f"字典转 JSON 失败: {e}")
        raise


# 格式转换：处理货币格式（如 '$123,456.78' -> '123456.78'）
def format_currency(currency_string: str) -> float:
    """
    将带有货币符号和逗号的字符串转换为 float
    :param currency_string: 货币格式字符串，如 '$123,456.78'
    :return: 数字格式
    """
    try:
        cleaned_string = re.sub(r'[^\d.]', '', currency_string)
        return float(cleaned_string)
    except ValueError as e:
        logging.error(f"货币格式转换失败: {e}")
        raise


# 示例：保存数据到文件
def save_data_to_file(file_name: str, data: Any):
    """
    将数据保存到文件
    :param file_name: 文件名
    :param data: 要保存的数据
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"数据成功保存到 {file_name}")
    except Exception as e:
        logging.error(f"保存数据失败: {e}")
        raise
