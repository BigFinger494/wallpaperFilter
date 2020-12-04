import unittest
import ezFilter as tested_app
import json
import os.path
class FilterScriptTests(unittest.TestCase):

    def setUp(self):
        tested_app.first= "\\newFolder"
       

    def test_create_new_folder(self):
        path = tested_app.createDirectory()
        self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()