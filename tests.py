import unittest
import ezFilter as tested_app
import json
import os.path
import argparse
import sys
class FilterScriptTests(unittest.TestCase):
    
    script = "jemima"
    path = "\\newFolder"
    def setUp(self):
        tested_app.first= "\\newFolder"
        tested_app.script = "\\newFolder"
       

    def test_create_new_folderTest(self):
        path = tested_app.createDirectory()
        self.assertTrue(os.path.exists(path))



if __name__ == '__main__':
    unittest.main()
