import unittest
from pytest import raises
from problems.costofconversion import ConversionExecutor, ConversionData

class TestCostOfConversion(unittest.TestCase):
    def test_valid(self):
        # Test case 1: Test with a valid input
        data = ConversionData("100", "asd", [0.1], [0.1], [0.1])
        executor = ConversionExecutor(data)
        try:
          result = executor.execute()
        except ValueError as e:
            self.fail(str(e))
        self.assertEqual(result, 0.2)

    def test_invalid(self):
        # Test case 2: Test with an invalid input origin is empty
        data = ConversionData("100", "asd", [], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)
        
        # Test case 3: Test with an invalid input origin is not an array
        data = ConversionData("100", "asd", 23, [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

        # Test case 4: Test with an invalid input source is not a string
        data = ConversionData([23], "asd", [23], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)
        
        # Test case 5: Test with an invalid input source is empty
        data = ConversionData("", "asd", [23], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

        # Test case 6: Test with an invalid input destination is not a string
        data = ConversionData("asd", [23], [23], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)
        
        # Test case 7: Test with an invalid input destination is empty
        data = ConversionData("asd", "", [23], [0.1], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

        # Test case 8: Test with an invalid input changed is not an array
        data = ConversionData("100", "asd", [0.1], 23, [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

        # Test case 9: Test with an invalid input changed is empty
        data = ConversionData("100", "asd", [0.1], [], [0.1])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)
        
        # Test case 10: Test with an invalid input cost is not an array
        data = ConversionData("100", "asd", [0.1], [0.1], 23)
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

        # Test case 11: Test with an invalid input changed is empty
        data = ConversionData("100", "asd", [0.1], [0.1], [])
        with raises(ValueError):
            executor = ConversionExecutor(data)
            result = executor.execute()
            self.assertNotEqual(result, 0.1)

if __name__ == '__main__':
    unittest.main()