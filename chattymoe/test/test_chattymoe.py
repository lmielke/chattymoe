# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
from chattymoe.chattymoe import Moe as PC


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
        with open(os.path.join(sts.testDataPath, "chattymoe.yml"), "r") as f:
            out = yaml.safe_load(f)
        return out

    def test__str__(self, *args, **kwargs):
        kwargs.update(self.testData)

        expected = (
            f"chattymoe.chattymoe.py"
        )
        pc = PC(*args, **kwargs)
        self.assertEqual(pc.__str__(*args, *kwargs), expected)


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
