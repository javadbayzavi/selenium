from functools import wraps

from selenium import webdriver


class WebDrivers:
    @staticmethod
    def enforce_chrome_driver(cls):
        return WebDrivers.enforce_webdriver(webdriver.Chrome)(cls)

    @staticmethod
    def enforce_firefox_driver(cls):
        return WebDrivers.enforce_webdriver(webdriver.Firefox)(cls)

    @staticmethod
    def enforce_webdriver(webdriver_class):
        def decorator(cls):
            original_init = cls.__init__
            original_setup = cls.setUp

            @wraps(original_setup)
            def new_setup(self, *args, **kwargs):
                original_setup(self, *args, **kwargs)
                if not hasattr(self, 'initialize_driver'):
                    raise NotImplementedError(f"{cls.__name__} must implement the method 'initialize_driver'.")

                def wrapper(*args, **kwargs):
                    result = self.initialize_driver(*args, **kwargs)
                    if not isinstance(self.driver, webdriver_class):
                        raise TypeError(f"{cls.__name__} must use {webdriver_class.__name__} for 'initialize_driver'.")
                    return result

                self.initialize_driver = wrapper

            cls.setUp = new_setup

            return cls

        return decorator
