'''配置解析工具'''

import configparser

config = configparser.ConfigParser()


class ConfParse:
    '''配置解析'''

    REDIS_CONF = '{}-redis'

    @classmethod
    def _get_env(cls, filename='../conf/config.ini'):
        '''
        获取线上还是线下
        '''
        config.read(filename, encoding='utf-8')
        return config.get('environ', 'env')

    @classmethod
    def get_redis_conf(cls):
        '''
        获取IP和端口号等信息
        :return:
        '''
        select_section = cls.REDIS_CONF.format(cls._get_env())
        return [config.get(select_section, item)
                for item in config.options(select_section)]
