from redis import Redis


class BaseConfig(object):
    # Flask-Session: 第二步配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='192.168.0.94', port='6379')

    # ##### SQLALchemy配置文件 #####
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/booktest?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 10  # 连接池
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


class ProConfig(BaseConfig):
    pass
