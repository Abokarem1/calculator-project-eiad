from BE.calculator_helper import CalculatorHelper
import pytest
from tests.test_unit_api import TestApi

@pytest.mark.parametrize( "eyad,expected",[("3 + 3", 6), ("2 + (-4)", -2)])    
def test_eval(eyad,expected):
    assert eval(eyad) == expected

class BaseTestSetupTeardown():
    def test_setup_teardown(self):
        self.calculator = CalculatorHelper()

class TestCalculator(BaseTestSetupTeardown):
    def test_add(self):
        calculator = CalculatorHelper()
        value = calculator.add(1,1)
        assert value == 2
    def test_sub(self):
        calculator = CalculatorHelper()
        value = calculator.subtract(1,1)
        assert value == 0
    def test_mult(self):
        calculator = CalculatorHelper()
        value = calculator.multiply(2,3)
        assert value == 6
    def test_divide(self):
        calculator = CalculatorHelper()
        value = calculator.divide(8,2)
        assert value == 4
    def test_division_by_zero(self):
        calculator = CalculatorHelper()
        with pytest.raises(ZeroDivisionError):
            calculator.divide(8,0)
        
