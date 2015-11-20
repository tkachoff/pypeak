from pypeak.driver import get_driver
from pypeak.errors import PyPeakException

__author__ = 'Artsiom Tkachou'


class BasePage(object):
    url = None

    @property
    def _driver(self):
        if self.__driver:
            return self.__driver
        return get_driver()

    def __init__(self, driver=None, url=None):
        if url:
            self.url = url
        self.__driver = driver

    def open(self):
        if not self.url:
            raise PyPeakException('Can\'t open page without url')
        self._driver.get(self.url)
