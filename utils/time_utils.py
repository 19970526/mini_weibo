'''时间工具类'''

import time


class TimeUtils:
    '''
    时间工具
    '''

    @classmethod
    def get_current_timestamp(cls):
        '''
        获取当前时间戳
        :return:
        '''
        return int(time.time())

    @classmethod
    def timestamp_to_str(cls, timestamp):
        '''
        时间戳转化成时间字符串
        :param timestamp:
        :return:
        '''

        return time.strptime('%Y-%m-%d %H:%H:%S', time.localtime(timestamp))
