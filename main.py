def verify_card_number(card_number):
    card_translation = str.maketrans({'-':'', ' ':''})
    translated_card_number = card_number.translate(card_translation)

    sum_of_odd_digits = 0
    translated_card_number_reversed = translated_card_number[::-1]
    odd_digits = translated_card_number_reversed[::2]
    sum_of_even_digits = 0
    even_digits = translated_card_number_reversed[1::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits

    return 'VALID!' if total % 10 == 0 else 'INVALID!'

print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
