# standard lib imports
import colorama as color

color.init()

import os, re, shutil, sys, time
import yaml
import unittest

# test package imports
import chattymoe.settings as sts
import chattymoe.helpers.markddown_to_python as test_module


# print(f"\n__file__: {__file__}")


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        cls.verbose = 0
        # cls.testData = cls.mk_test_data(*args, **kwargs)
        cls.mdFilePath = os.path.join(sts.testDataDir, "test_markdown_to_python_testfile.md")
        cls.pyFilePath = os.path.join(sts.testDataDir, "test_markdown_to_python_testfile.py")

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        pass

    # @classmethod
    # def mk_test_data(cls, *args, **kwargs):
    #     with open(os.path.join(sts.testDataDir, "response.txt"), "r") as f:
    #         out = f.read()
    #     return out

    def test_make_file_names(self, *args, **kwargs):
        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
        expected = os.path.join(sts.testDataDir, self.pyFilePath)
        mdFilePath, pyFilePath = test_module.make_file_names(
                                                                filePath, 
                                                                sts.testDataDir,
                                                                *args, **kwargs
                                                                )
        self.assertEqual(pyFilePath, expected)

    def test_load_file(self, *args, **kwargs):
        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
        expected = "# Test of Python and Markdown in one file"
        mdText = test_module.load_file(filePath, *args, **kwargs)
        self.assertEqual(mdText[:len(expected)], expected)

    def test_convert_markdown_to_python(self, *args, **kwargs):
        expected = '# <md>General imports'
        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
        mdText = test_module.load_file(filePath, *args, **kwargs)
        converted = test_module.convert_markdown_to_python(mdText, *args, **kwargs)
        self.assertTrue(expected in converted)

    def test_save_to_file(self, *args, **kwargs):
        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
        mdFilePath, pyFilePath = test_module.make_file_names(
                                                                filePath, 
                                                                sts.testDataDir,
                                                                *args, **kwargs
                                                                )
        mdText = test_module.load_file(mdFilePath, *args, **kwargs)
        converted = test_module.convert_markdown_to_python(mdText, *args, **kwargs)
        test_module.save_to_file(pyFilePath, converted, *args, **kwargs)
        from chattymoe.test.data.test_markdown_to_python_testfile import ping
        self.assertEqual(ping(), "pong")

    def test_convert_python_to_markdown(self, *args, **kwargs):
        time.sleep(.5)
        filePath = os.path.join(sts.testDataDir, self.pyFilePath)
        mdFilePath, pyFilePath = test_module.make_file_names(
                                                                filePath, 
                                                                sts.testDataDir,
                                                                *args, **kwargs
                                                                )
        pyText = test_module.load_file(pyFilePath, *args, **kwargs)
        converted = test_module.convert_python_to_markdown(pyText, *args, **kwargs)
        mdText = test_module.load_file(mdFilePath, *args, **kwargs)
        self.assertEqual(converted, mdText)


if __name__ == "__main__":
    unittest.main()
    print("done")
    exit()
