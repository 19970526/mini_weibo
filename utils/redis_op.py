'''redis相关操作'''

import json
import redis
from constant.constants import RedisKey
from model.wb_model import User
from utils.conf_parse import ConfParse
from utils.time_utils import TimeUtils


class RedisOp:
    '''
    redis操作
    '''

    conn = None

    @classmethod
    def crest_op(cls):
        '''
        创建连接
        :return:
        '''
        redis_conf = ConfParse.get_redis_conf()
        cls.conn = redis.StrictRedis(host=redis_conf[0], port=redis_conf[1])

    @classmethod
    def get_new_id(cls, key):
        '''
        根据提供的key获取id
        :return:
        '''

        return cls.incr(key)

    @classmethod
    def store_user_object(cls, user):
        '''
        存储用户对象
        :param user:
        :return:
        '''
        user.id = cls.get_new_id(RedisKey.USER_ID)
        cls.conn.set(RedisKey.USER_PREFIX.format(user.id), user.to_json)

        return user.id

    @classmethod
    def get_user_by_id(cls, user_id):
        '''
        通过user_id获取user_object
        :param user_id:
        :return:
        '''
        json_user = cls.conn.get(RedisKey.USER_PREFIX.format(user_id))
        user = User(0, 0, 0)
        user.__dict__.update(json.loads(json_user))

        return user

    @classmethod
    def stroe_user_attention(cls, user, attention_user):
        '''
        1.存储用户关注信息
        2.获取粉丝信息
        :param user:
        :param attention_user:
        :return:
        '''
        pipe = cls.conn.pipeline()
        pipe.rpush(RedisKey.USER_ATTENTION_PREFIX.format(user.id), attention_user.id)
        pipe.rpush(RedisKey.USER_FAMS_PREFIX.format(attention_user.id), user.id)
        pipe.execute()

    @classmethod
    def get_user_attention_ids(cls, user):
        '''
        获取用户关注的用户的ID
        :return:
        '''
        return cls.conn.lrange(RedisKey.USER_ATTENTION_PREFIX.format(user.id), 0, 1)

    @classmethod
    def get_user_fans_ids(cls, user):
        '''
        获取用户的粉丝的ID
        :param user:
        :return:
        '''
        return cls.conn.lrange(RedisKey.USER_FAMS_PREFIX.format(user.id), 0, 1)

    @classmethod
    def store_topic_object(cls, topic):
        '''
        存储话题对象
        :param topic:
        :return:
        '''

        topic.id = cls.get_new_id(RedisKey.TOPIC_ID)
        cls.conn.set(RedisKey.TOPIC_PREFIX.format(topic.id), topic.to_json)

        return topic.id

    @classmethod
    def join_in_topic(cls, user, topic_id):
        '''
        参与某个话题
        :param user:
        :param topic_id:
        :return:
        '''
        cls.conn.sadd(RedisKey.JOIN_IN_TOPIC_PREFIX.format(topic_id), user.id)

    @classmethod
    def store_weibo_object(cls, weibo):
        '''
        1.加入到自己的微博列表
        2.加入到粉丝的微博列表
        3.加入到微博广场中，且保留100条
        4.更新微博指数
        :param weibo:
        :return:
        '''
        weibo.timestamp = TimeUtils.get_current_timestamp()
        weibo.id = cls.get_new_id(RedisKey.WEIBO_ID)
        weibo_json_str = weibo.to_json

        fans_id_list = cls.conn.lrange(RedisKey.USER_FAMS_PREFIX.format(weibo.user_id), 0, -1)
        fans_list = [cls.get_user_by_id(fans_id) for fans_id in fans_id_list]

        pipe = cls.conn.pipeline()
        pipe.hset(RedisKey.USER_WEIBO_PREFIX.format(weibo.user_id), weibo.id, weibo_json_str)
        for fan in fans_list:
            pipe.lpush(RedisKey.USER_ATTENTION_WEIBO_PREFIX.format(fan.id), weibo_json_str)
        pipe.lpush(RedisKey.WEIBO, weibo_json_str)
        pipe.ltrim(RedisKey.WEIBO_INDEX, 0, 99)
        pipe.zincrby(RedisKey.WEIBO_INDEX, weibo.user_id, amount=1)
        pipe.execute()

        return weibo.id
