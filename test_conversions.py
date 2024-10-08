import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        """Tests the conversion from Celsius to Kelvin.

        Asserts that the conversion is correct for various input values.
        """
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0, places=2)

    def test_convertCelsiusToFahrenheit(self):
        """Tests the conversion from Celsius to Fahrenheit.

        Asserts that the conversion is correct for various input values.
        """
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40.0, places=2)

if __name__ == '__main__':
    
    unittest.main()