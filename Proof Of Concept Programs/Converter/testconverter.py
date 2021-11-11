import unittest
import os

from converter import Converter

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()
        self.bytes = b'00401019 CC CC CC	CC CC CC CC'
        self.testdir = "/testdir"
        self.filetest = "/testdir/testfile.txt"

    def setDir(self):
        os.makedirs(os.path.dirname(self.filetest), exist_ok=True)
        with open(self.filetest, 'wb') as f:
            f.write(self.bytes) 
            f.close()

    def test_getBinData(self):
        self.setDir()
        expected = list(self.bytes)
        output = self.converter.getBinaryData(self.filetest)
        for b in range(len(output)):
            self.assertEqual(output[b], expected[b], 'Ouput byte is not equal to expected byte.')
    
    def tearDown(self):
        if os.path.exists(self.filetest):
            os.remove(self.filetest)

if __name__ == '__main__':
    unittest.main()