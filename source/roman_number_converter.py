import sys
sys.path.append("..")
from config.config import special_nums


class RomanNumeralsConverter():
    

    def roman_converter(self, number):
        roman_letter = ""
        
        if (number > 4000) or (number <= 0):
            raise ValueError("Number should be greater than 0 and less than 4000")
        
        if number >= 1000:
            rem_1000, number = divmod(number, 1000)
            roman_letter = roman_letter + rem_1000 * special_nums[1000]
        
        if (number >= (1000 - 100)):
            if (number < 1000):
                roman_letter = roman_letter + special_nums[100]
                number = number + 100
            roman_letter = roman_letter + special_nums[1000]
            number = number - 1000
            
        if (number >= (500 - 100)):
            if (number < 500):
                roman_letter = roman_letter + special_nums[100]
                number = number + 100
            roman_letter = roman_letter + special_nums[500]
            number = number -  500
        
        if number >= 100:
            rem_100, number = divmod(number, 100)
            roman_letter = roman_letter + rem_100 * special_nums[100]

        if (number >= (100 - 10)):
            if (number < 100):
                roman_letter = roman_letter + special_nums[10]
                number = number + 10
            roman_letter = roman_letter + special_nums[100]
            number = number - 100
        
        if (number >= (50 - 10)):
            if (number < 50):
                roman_letter = roman_letter + special_nums[10]
                number = number + 10
            roman_letter = roman_letter + special_nums[50]
            number = number -  50
            
        if number >= 10:
            rem_10, number = divmod(number, 10)
            roman_letter = roman_letter + rem_10 * special_nums[10]

        if (number >= (10 - 1)):
            if (number < 10):
                roman_letter = roman_letter + special_nums[1]
                number = number + 1
            roman_letter = roman_letter + special_nums[10]
            number = number - 10
        
        if (number >= (5 - 1)):
            if (number < 5):
                roman_letter = roman_letter + special_nums[1]
                number = number + 1
            roman_letter = roman_letter + special_nums[5]
            number = number -  5

        roman_letter = roman_letter + (number * special_nums[1])
        return str(roman_letter)
    
if __name__ == "__main__":
    number = 21
    roman_converter_obj = RomanNumeralsConverter()
    try:
        roman_letter = roman_converter_obj.roman_converter(number)
        print("Converted Roman Numberal: ", number, "->",roman_letter)
    except Exception as e:
        print("Error:", str(e))