from logging import Logger
from selenium.webdriver import Firefox

class Settings(object):
    driver_cls = Firefox
    logger_cls = Logger
    implicit_timeout = 30
    wait_timeout = 30

    @classmethod
    def set_driver_class(cls, clazz):
        cls.driver_cls = clazz
