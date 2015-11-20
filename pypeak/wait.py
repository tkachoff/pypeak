from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pypeak.driver import get_driver
from pypeak.settings import Settings


def wait_until_html_element_disappear(locator):
    wait = WebDriverWait(get_driver(), Settings.wait_timeout)
    wait.until(EC.invisibility_of_element_located((locator.by, locator.value)))


def _ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        return False


def wait_jquery(timeout=30):
    wait = WebDriverWait(get_driver(), timeout)
    try:
        wait.until(_ajax_complete)
    except TimeoutException:
        print("Jquery is still active")
