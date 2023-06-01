import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_saccess(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsaccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_multiply_saccess(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_subtraction_saccess(self):
        assert self.calc.subtraction(self, 8, 5) == 3

    def test_division_saccess(self):
        assert self.calc.division(self, 36, 6) == 6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

