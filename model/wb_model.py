'''微博中涉及对象的定义'''

import json


class ToJson:
    '''对象转json'''

    @property
    def to_json(self):
        return json.dumps(self.__dict__)


class User(ToJson):
    '''用户对象'''

    def __init__(self, name, age, signature=''):
        '''
        初始化函数
        :param name:
        :param age:
        :param signature:
        '''

        self.id = -1
        self.name = name
        self.age = age
        self.signature = signature

    @property
    def sign(self):
        return self.signature

    @sign.setter
    def sign(self, signature):
        self.signature = signature


class WeiBo(ToJson):
    '''微博对象'''

    def __init__(self, user_id, text, click_count=0):
        '''
        初始化函数
        :param user_id:
        :param text:
        :param click_count:
        '''

        self.id = -1
        self.user_id = user_id
        self.text = text
        self.click_count = click_count
        self.timestamp = 0

    @property
    def click(self):
        return self.click_count

    @click.setter
    def click(self, click_count):
        self.click = click_count


class Topic(ToJson):
    '''话题对象'''

    def __init__(self, logo, text):
        '''
        初始化函数
        :param logo:
        :param text:
        '''

        self.id = -1
        self.logo = logo
        self.text = text
