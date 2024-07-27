import unittest
from pytest import raises
from problems.costofconversion import ConversionExecutor, ConversionData

class TestCostOfConversion(unittest.TestCase):
    def test_valid(self):
        # Test case 1: Test with a valid input
        data = ConversionData([100, 200], [0.1], [0.1], [0.1], [0.1])
        executor = ConversionExecutor(data)
        try:
          result = executor.execute()
        except ValueError as e:
            self.fail(str(e))
        self.assertEqual(result, 0.2)

    def test_invalid(self):
        # Test case 2: Test with an invalid input that throws error
        data = ConversionData([100, 200], [], [], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

if __name__ == '__main__':
    unittest.main()