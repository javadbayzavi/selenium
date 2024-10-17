from abc import abstractmethod


class DriverSettings:
    def __init__(self):
        pass

    def is_headless(self):
        return '--headless' in self.get_options().arguments

    @abstractmethod
    def get_options(self):
        pass
