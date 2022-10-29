from config.config import special_nums


class RomanNumeralsConverter():
    
    
    def roman_converter(number):
        roman_letter = ""

        if (number > 4000) or (number <= 0):
            raise ValueError("Number should be greater than 0 and less than 4000")
        
        if number >= 1000:
            rem_1000, number = divmod(number, 1000)
            roman_letter = roman_letter + rem_1000 * special_nums[1000]
            
        
        if number >= 500:
            rem_500, number = divmod(number, 500)
            roman_letter = roman_letter + rem_500 * special_nums[500]
            
        if number >= 400:
            rem_400, number = divmod(number, 400)
            roman_letter = roman_letter + rem_400 * special_nums[400]
            
        if number >= 100:
            rem_100, number = divmod(number, 100)
            roman_letter = roman_letter + rem_100 * special_nums[100]
        
        if number >= 50:
            rem_50, number = divmod(number, 50)
            roman_letter = roman_letter + rem_50 * special_nums[40]
        
        if number >= 40:
            rem_40, number = divmod(number, 40)
            roman_letter = roman_letter + rem_40 * special_nums[40]
            
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
        return roman_letter

if __name__ == "__main__":
    number = 1111
    try:
        roman_letter = RomanNumeralsConverter.roman_converter(number)
        print("Converted Roman Numberal: ", number, "->",roman_letter)
    except Exception as e:
        print("Error:", str(e))