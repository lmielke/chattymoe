# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
from chattymoe.actions import chat


# print(f"\n__file__: {__file__}")


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        cls.verbose = 0
        # cls.testData = cls.load_test_data(*args, **kwargs)

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        pass

    def load_test_data(cls, fileName, *args, **kwargs):
        with open(os.path.join(sts.testDataDir, fileName), "r") as f:
            out = yaml.safe_load(f)
        return out

    def test_comunicate(*args, **kwargs):
        lang = 'en'
        text = 'This is a test' if lang == 'en' else 'Dies ist ein Test'
        chat.communicate(text, *args, lang=lang, origin='audio', verbose=1,  **kwargs)


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
