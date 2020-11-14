from pymeetings.utils import *
import unittest



class TestCountry(unittest.TestCase):

    def test_type(self):
        city = 'Paris'
        assert isinstance(country(city), str)
                
    def test_correctness(self):
        pass
        
class TestCityCheck(unittest.TestCase):

    def test_type(self):
        city = 'Paris'
        assert isinstance(citycheck(city), bool)

    def test_correctness(self):
        pass
        



if __name__ == '__main__':
    unittest.main()
