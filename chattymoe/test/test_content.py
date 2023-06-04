# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
from chattymoe.content import Content as PC


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

    def test_get_text(self, *args, **kwargs):
        expected = '## Your Identy:'
        testData = self.load_test_data('test_content.yml')
        ti = PC(*args, origin=None, **kwargs)
        out = ti.get_text(*args, content=testData[0].get('content'), **kwargs)
        self.assertTrue(out.strip().startswith(expected))
        # test from_stdout
        expected = 'Not implemented yet!'
        ti = PC(*args, origin='system', **kwargs)
        out = ti.get_text(*args, content=testData[0].get('content'), **kwargs)
        self.assertTrue(out.strip().startswith(expected))


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
