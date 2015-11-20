from pypeak.driver import get_driver

__author__ = 'Artsiom Tkachou'

from pypeak.wait import wait_jquery


class HtmlElement(object):
    def __init__(self, locator=None, waiter=wait_jquery, wrapped_element=None, cached=False):
        if locator is not None:
            self.by = locator.by
            self.value = locator.value
        self.waiter = waiter
        self.cached = cached
        self.wrapped_element = wrapped_element

    def __get__(self, instance, owner):
        self.parent = instance
        if self.cached:
            return self
        self.wrapped_element = self._find_element()
        return self

    def _find_element(self):
        # self.waiter()
        return self.get_finder().find_element(self.by, self.value)

    def get_finder(self):
        if isinstance(self.parent, HtmlElement):
            return self.parent.wrapped_element
        else:
            return get_driver()
