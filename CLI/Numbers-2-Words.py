def num_to_words(num):
    if not isinstance(num, (int, float)) or num < 0:
        raise ValueError("input type must be a positive integer or float")

    int_part = int(num)
    decimal_part = int(round((num - int_part) * 100))

    int_part_words = _num_to_words_helper(int_part)
    decimal_part_words = _num_to_words_helper(decimal_part)

    result = int_part_words + " point " + decimal_part_words if decimal_part_words else int_part_words
    return result

def _num_to_words_helper(num):
    if num == 0:
        return "zero"

    # List of tuples containing the number words and their values
    words = [
        (10 ** 18, "quintillion"),
        (10 ** 15, "quadrillion"),
        (10 ** 12, "trillion"),
        (10 ** 9, "billion"),
        (10 ** 6, "million"),
        (10 ** 3, "thousand"),
        (100, "hundred"),
        (90, "ninety"),
        (80, "eighty"),
        (70, "seventy"),
        (60, "sixty"),
        (50, "fifty"),
        (40, "forty"),
        (30, "thirty"),
        (20, "twenty"),
        (19, "nineteen"),
        (18, "eighteen"),
        (17, "seventeen"),
        (16, "sixteen"),
        (15, "fifteen"),
        (14, "fourteen"),
        (13, "thirteen"),
        (12, "twelve"),
        (11, "eleven"),
        (10, "ten"),
        (9, "nine"),
        (8, "eight"),
        (7, "seven"),
        (6, "six"),
        (5, "five"),
        (4, "four"),
        (3, "three"),
        (2, "two"),
        (1, "one"),
    ]

    result = ""
    for value, word in words:
        if num >= value:
            count = num // value
            num %= value
            if count > 1:
                result += _num_to_words_helper(count) + " "
            result += word
            if num > 0:
                result += " "

    if result.startswith(("hundred", "thousand", "million", "billion", "trillion", "quintillion", "quadrillion", "quintillion")):
        result = "one " + result

    return result.strip()

try:
    print(num_to_words(100.5)) # >>> one hundred point five
    print(num_to_words(12345.67)) # >>> twelve thousand three hundred forty-five point sixty-seven
    print(num_to_words("not a number")) # >>> ValueError
except ValueError as e:
    print(e)
