# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
from chattymoe.response import Response as TC


# print(f"\n__file__: {__file__}")


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        cls.verbose = 0
        cls.testData = cls.mk_test_data(*args, **kwargs)

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        pass

    @classmethod
    def mk_test_data(cls, *args, **kwargs):
        with open(os.path.join(sts.testDataPath, "response.txt"), "r") as f:
            out = f.read()
        return out

    def test_clean_response(self, *args, **kwargs):
        start, end = "Get-ChildItem", "}"
        ti = TC(self.testData, *args, **kwargs)
        out = ti.clean_response(*args, *kwargs)
        self.assertTrue(out.startswith(start) and out.endswith(end))


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
