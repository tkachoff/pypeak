from selenium.webdriver import Firefox

from pypeak import All
from pypeak.base_page import BasePage
from pypeak.driver import close_driver
from pypeak.element import Text, Button, HtmlElement, Link, TextInput
from pypeak.locator import Name, XPath, ID
from pypeak.settings import Settings

__author__ = 'Artsiom Tkachou'


class GooglePage(BasePage):
    url = "http://www.google.com"

    text_field = TextInput(Name('q'))
    button = Button(Name('btnK'))


class ResultItem(HtmlElement):
    header = Link(XPath('.//h3/a'))
    link = Link(XPath(''))


class ResultsPage(object):
    stat = Text(ID('resultStats'))
    results = All(ResultItem, XPath("//div[@class='srg']/div"))


if __name__ == '__main__':
    Settings.set_driver_class(Firefox)
    home_page = GooglePage()
    home_page.open()
    home_page.text_field.send_keys('Page Object')
    home_page.button.click()
    results_page = ResultsPage()
    print('Results summary: {0}'.format(results_page.stat.text))
    for item in results_page.results:
        print(item.header.text)
    close_driver()
