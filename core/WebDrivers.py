from enum import Enum
from functools import wraps

class WebDrivers:
    @staticmethod
    def enforce_chrome_driver(cls_or_isLocal=None):
        # If called without parentheses, cls_or_isLocal is the class itself
        if isinstance(cls_or_isLocal, type):
            return WebDrivers.enforce_webdriver(browser_type="chrome")(cls_or_isLocal)
        else:
            isLocal = cls_or_isLocal if cls_or_isLocal is not None else False
            return WebDrivers.enforce_webdriver(browser_type="chrome", isLocal=isLocal)

    @staticmethod
    def enforce_firefox_driver(cls_or_isLocal=None):
        # If called without parentheses, cls_or_isLocal is the class itself
        if isinstance(cls_or_isLocal, type):
            return WebDrivers.enforce_webdriver(browser_type="firefox")(cls_or_isLocal)
        else:
            isLocal = cls_or_isLocal if cls_or_isLocal is not None else False
            return WebDrivers.enforce_webdriver(browser_type="firefox", isLocal=isLocal)

    @staticmethod
    def enforce_webdriver(browser_type, isLocal: bool = False):
        def decorator(cls):
            cls._webdriver_type = browser_type
            cls._is_local = isLocal
            original_setup = cls.setUp

            @wraps(original_setup)
            def new_setup(self, *args, **kwargs):
                original_setup(self, *args, **kwargs)
                if not hasattr(self, 'initialize_driver'):
                    raise NotImplementedError(f"{cls.__name__} must implement the method 'initialize_driver'.")

            cls.setUp = new_setup
            return cls

        return decorator
