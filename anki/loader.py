import json

from datetime import datetime


def json_loader(file_path, encoding='utf-8'):
    with open(file_path, encoding=encoding) as file:
        json_data = json.load(file)

    data_list = []
    for data in json_data:
        data_list.append([
            data.get('type'),
            data.get('original_content'),
            data.get('romaji_content'),
            data.get('translated_content'),
            data.get('explanation')])

    return data_list


def str2time(time_str, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(time_str, format)


def time2str(time, format="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format)
