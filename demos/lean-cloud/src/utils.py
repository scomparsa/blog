# -*- coding:utf8 -*-

import time
import datetime

def transfer_normal_params(args):
    try:
        dic = {}
        for key, value in args.items():
            dic[key] = get_first_item(value)
        return True, dic
    except:
        return False, None

def get_first_item(item):
    if isinstance(item, type(None)):
        return ""
    elif isinstance(item, list):
        if len(item) > 0:
            return item[0]
        return ""
    elif isinstance(item, str):
        return item

def datetime_to_str(dt, without_second=True):    
    return dt.strftime('%Y-%m-%d %H:%M:%S') if not without_second else dt.strftime('%Y-%m-%d %H:%M')

def str_to_datetime(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

def str_to_timestamp(str):
    return int(time.mktime(str_to_datetime(str).timetuple()))

def timestamp_to_date(t, show_time=False, show_second=True):
    _format = "%Y-%m-%d"
    if show_time:
        if show_second:
            _format = _format + " %H:%M:%S"
        else:
            _format = _format + " %H:%M"
    return time.strftime(_format, time.localtime(int(t)))