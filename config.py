#-*- coding= utf-8 -*-
import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG=True  #开发调试环境

class TestingConfig(Config):
    TESTING=True   #测试环境

class ProductionConfig(Config):
    pass   #生产环境

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}