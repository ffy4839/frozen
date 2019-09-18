from bin.func import *


class main():
    def __init__(self, config_data):
        self.BAUDRATE = int(config_data['baudrate'])  # 波特率
        self.FROZEN_HOUR_TIMES = int(config_data['frozen_hour'])  # 小时冻结次数
        self.FROZEN_DAY_TIMES = int(config_data['frozen_day'])  # 天冻结次数
        self.FROZEN_MONTH_TIME = int(config_data['frozen_month'])  # 月冻结次数
        self.INTERVAL = int(config_data['interval'])  # 两次设置间隔
        self.MONTH_FROZEN_DAY = eval(config_data['month_frozen_day'])  # 月冻结时间

        self.LEADING = int(config_data['leading']) * '55'

class initbase():
    def __init__(self):
