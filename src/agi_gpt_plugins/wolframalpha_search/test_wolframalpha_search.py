import os
import unittest

import requests

from . import AgiGptWolframAgiGptSearch


class TestAgiGptWolframAgiGptSearch(unittest.TestCase):
    def setUp(self):
        os.environ["WOLFRAMagi-gpt_APPID"] = "test_appid"
        self.plugin = AgiGptWolframAgiGptSearch()

    def tearDown(self):
        os.environ.pop("WOLFRAMagi-gpt_APPID", None)

    def test_wolframagi-gpt_search(self):
        query = "2+2"
        try:
            from .wolframagi-gpt_search import _wolframagi-gpt_search
            _wolframagi-gpt_search(query)
        except requests.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
