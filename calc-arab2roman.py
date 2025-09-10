class CalculatorError(Exception):
    """Класс для обработки ошибок калькулятора."""
    pass

def roman_to_arabic(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    value = 0
    prev_value = 0
    for char in reversed(roman):
        current_value = roman_numerals[char]
        if current_value < prev_value:
            value -= current_value
        else:
            value += current_value
        prev_value = current_value
    return value

def arabic_to_roman(num):
    if num <= 0:
        return ''   
    arabic_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, numeral in arabic_to_roman_map:
        while num >= value:
            result += numeral
            num -= value
    return result

def calculate(expression):
    try:
         parts = expression.split()
        if len(parts) != 3:
            raise CalculatorError("Формат выражения должен быть: 'число оператор число'")
        
        left, operator, right = parts

         is_left_roman = left.isalpha()
        is_right_roman = right.isalpha()

        if is_left_roman != is_right_roman:
            raise CalculatorError("Нельзя смешивать арабские и римские числа")
        
        if is_left_roman:
            left = roman_to_arabic(left)
            right = roman_to_arabic(right)
        else:
            left = int(left)
            right = int(right)
        
         if operator == '+':
            result = left + right
        elif operator == '-':
            result = left - right
        elif operator == '*':
            result = left * right
        elif operator == '/':
            if right == 0:
                raise CalculatorError("Деление на ноль невозможно")
            result = left // right
        else:
            raise CalculatorError("Неверный оператор. Допустимы: +, -, *, /")
        
         if is_left_roman:
            return arabic_to_roman(result)
        return str(result)
    except ValueError:
        raise CalculatorError("Некорректные числа")
    except CalculatorError as e:
        raise e

 print(calculate('1 + 2'))           # '3'
print(calculate('VI / III'))        # 'II'
print(calculate('VII / III'))       # 'II'
print(calculate('I + II'))          # 'III'
print(calculate('I - II'))          # ''
try:
    print(calculate('I + 1'))       # Exception
except CalculatorError as e:
    print(e)
try:
    print(calculate('1 + 1 + 1'))   # Exception
except CalculatorError as e:
    print(e)
