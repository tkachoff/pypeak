from random import choice

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as WebDriverSelect

from pypeak.element import HtmlElement

__author__ = 'Artsiom Tkachou'


class Button(HtmlElement):
    def click(self):
        self.wrapped_element.click()


class CheckBox(HtmlElement):
    def check(self):
        if not self.wrapped_element.is_selected():
            self.wrapped_element.click()

    def uncheck(self):
        if self.wrapped_element.is_selected():
            self.wrapped_element.click()


class Image(HtmlElement):
    @property
    def width(self):
        return self.wrapped_element.rect['width']

    @property
    def height(self):
        return self.wrapped_element.rect['height']

    def has_size(self):
        return True if self.width > 0 and self.height > 0 else False

    @property
    def alternate_text(self):
        """
        Returns value of ``alt`` attribute:
        """
        return self.wrapped_element.get_attribute('alt')


class Link(HtmlElement):
    def get_href(self):
        self.wrapped_element.get_attribute('href')

    def click(self):
        self.wrapped_element.click()

    @property
    def text(self):
        return self.wrapped_element.text


class Select(HtmlElement):
    @property
    def current_option(self):
        try:
            opt = WebDriverSelect(self.wrapped_element).first_selected_option
        except NoSuchElementException:
            return None
        return opt.text

    def get_values(self):

        options = WebDriverSelect(self.wrapped_element)._el.find_elements(
            By.CSS_SELECTOR, "option")
        if not options:
            return None
        return [option.get_attribute('value') for option in options]

    def get_options(self):
        """
        Returns a list of all options as web elements
        """
        return WebDriverSelect(self.wrapped_element).options

    def select_random(self):
        try:
            WebDriverSelect(
                self.wrapped_element).first_selected_option.get_attribute(
                'value')
        except NoSuchElementException:
            return
        values = self.get_values()
        WebDriverSelect(self.wrapped_element).select_by_value(choice(values))

    def select_by_visible_text(self, text):
        WebDriverSelect(self.wrapped_element).select_by_visible_text(text)

    def select_by_value(self, value):
        WebDriverSelect(self.wrapped_element).select_by_value(value)

    def select_by_index(self, index):
        WebDriverSelect(self.wrapped_element).select_by_index(index)


class TextInput(HtmlElement):
    def send_keys(self, text):
        self.wrapped_element.send_keys(text)

    def clear(self):
        self.wrapped_element.clear()

    def type(self, text):
        self.clear()
        self.send_keys(text)

    @property
    def text(self):
        return self.wrapped_element.get_attribute('value')


class Text(HtmlElement):
    @property
    def text(self):
        return self.wrapped_element.text
