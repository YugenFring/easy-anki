import json

from datetime import datetime


def json_loader(file_path, encoding='utf-8'):
    with open(file_path, encoding=encoding) as file:
        json_data = json.load(file)
    return json_data


def str2time(time_str, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(time_str, format)


def time2str(time, format="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format)
