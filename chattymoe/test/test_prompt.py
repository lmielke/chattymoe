# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
from chattymoe.prompt import Prompt as PC


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

    def test_handle_contents(self, *args, **kwargs):
        in_entry = {'content': '', 'meta': [None, 0], 'role': ''}
        expected = {'content': 'Hello there!', 'meta': [None, 0], 'role': ''}
        ti = PC(*args, **kwargs)
        entry = ti.handle_contents(in_entry, *args, **kwargs)
        self.assertEqual(entry, expected)
        # test_from_stdout
        expected = {'content': 'Not implemented yet!', 'meta': [None, 0], 'role': ''}
        ti = PC(*args, **kwargs)
        entry = ti.handle_contents(in_entry, *args, origin='system', running=True, **kwargs)
        self.assertEqual(entry, expected)

    def test_create_prompt(self, *args, **kwargs):
        expected = {'content': 'Hello there!', 'meta': [None, 0], 'role': 'system'}
        ti = PC(*args, **kwargs)
        entry = ti.create_prompt(*args, verbose=0, origin='system', **kwargs)
        self.assertEqual(entry, expected)
        # test_from_stdout
        expected = {'content': 'Not implemented yet!', 'meta': [None, 0], 'role': 'system'}
        ti = PC(*args, **kwargs)
        entry = ti.create_prompt(*args,  verbose=0, origin='system', running=True, **kwargs)
        self.assertEqual(entry, expected)
        # test_from_stdout
        text = self.load_test_data('test_content.yml')[-1].get('content')
        expected = {'content': text.replace('<colon>', ': '), 'meta': [None, 0], 'role': 'system'}
        ti = PC(*args, **kwargs)
        entry = ti.create_prompt(*args, content=text, verbose=0, origin='system', running=True, **kwargs)
        # print(entry)
        self.assertEqual(entry, expected)


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
