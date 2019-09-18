import serial
import configparser
import os
import binascii
import sys
import re
import time
import threading
import serial.tools.list_ports as LP

def time_now(st='%Y-%m-%d %H:%M:%S'):
    return time.strftime(st,time.localtime(time.time()))

def log(data):
    res = '{} | {}'.format(time_now(), str(data))
    save(res, name='ErrLog')
    print(res)

def show(data):
    res = '{} | {}'.format(time_now(), str(data))
    save(res, name='save')
    print(res)

def save(data, name='save', mode='a'):
    file_path = os.getcwd() + os.path.sep + name + '.txt'
    try:
        with open(file_path, mode) as f:
            f.write(data)
            f.write('\n')
    except Exception as e:
        print('{} | {}'.format(time_now(), str(e)))

def get_config(sections):
    data = {}
    config = configparser.ConfigParser()
    path = os.getcwd() + os.path.sep
    if 'setConfig.ini' in os.listdir(path):
        config.read(path + 'setConfig.ini', encoding='UTF-8')
        for i in config.items(section=sections):
            data[i[0]] = i[1]
        return data

    else:
        config['configs'] = {}
        config['configs']['baudrate'] = '9600'
        config['configs']['frozen_hour'] = '24'
        config['configs']['frozen_day'] = '3'
        config['configs']['frozen_month'] = '2'
        config['configs']['interval'] = '30'
        config['configs']['month_frozen_day'] = 'None'
        config['configs']['leading'] = '500'
        with open(path + 'setConfig.ini', 'w') as f:
            config.write(f)
        input('创建成功, 重启后开始冻结')
        sys.exit()

