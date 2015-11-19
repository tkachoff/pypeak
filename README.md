# PyPeak

PyPeak is a Page Object pattern implementation library for Python.

With the help of the PyPeak framework you can group web-page elements into blocks, encapsulate logic of interaction within them and then easily use created blocks in page objects.

To create custom web elements you should extend HtmlElement class to your custom controls like TextInput, Button and group them as pages.

Main classes are:
  
  Selectors:

- pypeak.selector.ID
- pypeak.selector.XPath
- pypeak.selector.ClassName
- pypeak.selector.TagName
- pypeak.selector.Name
- pypeak.selector.CssSelector
- pypeak.selector.LinkText
- pypeak.selector.PartialLinkText

  Elements:

- pypeak.element.HtmlElement
- pypeak.element.Button
- pypeak.element.TextInput
- pypeak.element.CheckBox
- pypeak.element.Select
- pypeak.element.Image
- pypeak.element.Text
- pypeak.element.Link

  Base:

- pypeak.All
- pypeak.BasePage

Basic usage example:

```python

from pypeak.selector import ID, Name, XPath
from pypeak.element import Link
from pypeak.driver import get_driver
from pypeak import BasePage, All


class GooglePage(BasePage):
    url = 'http://www.google.com'

    text_field = Text(Name('q'))
    button = Button(Name('btnK'))


class ResultItem(HtmlElement):
    link = Link(XPath('.//h3/a'))


class ResultsPage(BasePage):
    stat = Text(ID('resultStats'))
    results = All(ResultItem, XPath('//div/li'))


if __name__ == '__main__':
    home_page = GooglePage()
    home_page.open()
    home_page.text_field.send_keys('Page Object')
    home_page.button.click()
    results_page = ResultsPage()
    print 'Results summary: %s' % results_page.stat.text
    for item in results_page.results:
        print item.link.text
    get_driver().quit()
```

