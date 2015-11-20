from pypeak.settings import Settings

_driver_instance = None


def get_driver():
    global _driver_instance
    if not _driver_instance:
        _driver_instance = Settings.driver_cls()
        _driver_instance.implicitly_wait(Settings.implicit_timeout)
    return _driver_instance


def get_driver_no_init():
    return _driver_instance


def close_driver():
    global _driver_instance
    if _driver_instance:
        _driver_instance.quit()
        _driver_instance = None
