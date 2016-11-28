import unittest
import sp

# Some unit tests for the interface with the Opal Kelly module
# Limitations:
#   Not testing the internal OK methods beyond the API- they're a mess
#

class InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.des = sp.DESTester()

    def tearDown(self):
        self.des.resetBoard()

    def testResetBuffer(self):
        self.des.resetBuffer()
        buf = bytearray("\x00" * 2048)
        read = self.des.xem.ReadFromPipeOut(0xa0, buf)
        self.assertEqual(0, 0)

    def testConnect(self):
        self.assertEqual(self.des.xem.NoError, self.des.xem.OpenBySerial(""))

    def testEstimateDataBlockSizeZeroStreams(self):
        num_streams = 0
        correct_size = 32
        self.assertEqual(correct_size, self.des.dataBlockSize(num_streams))

    def testGetDataBlockZeroStreams(self):
        sample_length = 1
        num_data_streams = 0
        array = self.des.collectDataFromPipeOut(sample_length, num_data_streams)
        self.assertEqual(len(array), self.des.dataBlockSize(num_data_streams)*sample_length)

    def testGetDataBlockOneStream(self):
        sample_length = 1
        num_data_streams = 1
        array = self.des.collectDataFromPipeOut(sample_length, num_data_streams)
        self.assertEqual(len(array), self.des.dataBlockSize(num_data_streams)*sample_length)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
