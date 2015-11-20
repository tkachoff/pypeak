from selenium.webdriver.remote.webelement import WebElement

from pypeak.driver import get_driver
from pypeak.element import HtmlElement
from pypeak.wait import wait_jquery

__author__ = 'Artsiom Tkachou'


class All(object):
    def __init__(self, element_type=WebElement, locator=None,
                 waiter=wait_jquery):
        self.element_type = element_type
        self.by = locator.by
        self.value = locator.value
        self.waiter = waiter

    def __get__(self, instance, owner):
        self.parent = instance
        return self._find_elements()

    def _find_elements(self):
        if isinstance(self.parent, HtmlElement):
            finder = self.parent.wrapped_element
        else:
            finder = get_driver()
        # self.waiter()
        web_elements = finder.find_elements(self.by, self.value)
        if issubclass(self.element_type, WebElement):
            return web_elements
        else:
            return [self.element_type(wrapped_element=webelement, cached=True)
                    for webelement in
                    web_elements]
