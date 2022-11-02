import sys
sys.path.append("..")
# print(path)
from source.roman_number_converter import RomanNumeralsConverter
import pytest

roman_converter_obj = RomanNumeralsConverter()

def test_1():
    num_int = 1
    assert roman_converter_obj.roman_converter(num_int) == "I"

def test_2():
    num_int = 2
    assert roman_converter_obj.roman_converter(num_int) == "II"

def test_3():
    num_int = 3
    assert roman_converter_obj.roman_converter(num_int) == "III"

def test_4():
    num_int = 4
    assert roman_converter_obj.roman_converter(num_int) == "IV"

def test_5():
    num_int = 5
    assert roman_converter_obj.roman_converter(num_int) == "V"

def test_6():
    num_int = 6
    assert roman_converter_obj.roman_converter(num_int) == "VI"

def test_7():
    num_int = 7
    assert roman_converter_obj.roman_converter(num_int) == "VII"

def test_8():
    num_int = 8
    assert roman_converter_obj.roman_converter(num_int) == "VIII"

def test_9():
    num_int = 9
    assert roman_converter_obj.roman_converter(num_int) == "IX"

def test_21():
    num_int = 21
    assert roman_converter_obj.roman_converter(num_int) == "XXI"

def test_50():
    num_int = 50
    assert roman_converter_obj.roman_converter(num_int) == "L"

def test_100():
    num_int = 100
    assert roman_converter_obj.roman_converter(num_int) == "C"

def test_500():
    num_int = 500
    assert roman_converter_obj.roman_converter(num_int) == "D"

def test_1000():
    num_int = 1000
    assert roman_converter_obj.roman_converter(num_int) == "M"



