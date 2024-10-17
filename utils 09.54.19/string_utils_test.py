import unittest

from utils import string_utils


class StringUtilsTest(unittest.TestCase):

    def test_generate_email_with_defaults(self):
        email = string_utils.generate_random_email()
        self.assertRegex(email, r'selenium_[0-9a-z]{10}@3t\.io')

    def test_generate_email(self):
        email = string_utils.generate_random_email("my_domain.com", 42)
        self.assertRegex(email, r'selenium_[0-9a-z]{42}@my_domain\.com')
