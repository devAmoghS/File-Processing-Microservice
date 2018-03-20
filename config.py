class Config(object):
    """docstring for ClassName"""
    DEBUG = True
    TESTING = False
    DATABASE_NAME = "papers"


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig"""
    SECRET_KEY = "S0m3S3cr3tK3y"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
