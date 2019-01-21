'''常量定义'''


class RedisKey:
    '''
    redis 涉及到的 key定义
    '''

    # 用户ID生成计数
    USER_ID = 'user_id'
    # 微博ID生成计数
    WEIBO_ID = 'weibo_id'
    # 话题ID生成计数
    TOPIC_ID = 'topic_id'
    # 用户个人信息
    USER_PREFIX = 'user_%s'
    # 话题信息
    TOPIC_PREFIX = 'topic_%s'
    # 参与话题的用户存储
    JOIN_IN_TOPIC_PREFIX = 'join_in_topic_%s'
    # 用户发表的微博
    USER_WEIBO_PREFIX = 'user_weibo_%s'
    # 用户关注其他的用户
    USER_ATTENTION_PREFIX = 'user_attention_%s'
    # 用户关注发表的微博
    USER_ATTENTION_WEIBO_PREFIX = 'user_attention_weibo_%s'
    # 用户的粉丝
    USER_FAMS_PREFIX = 'user_fans_%s'
    # 微博广场
    WEIBO = 'weibo'
    # 用户指数
    WEIBO_INDEX = 'weibo_index'
