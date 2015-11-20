from pypeak.settings import Settings

_logger_instance = None


def get_logger():
    global _logger_instance
    if not _logger_instance:
        _logger_instance = Settings.logger_cls()
    return _logger_instance