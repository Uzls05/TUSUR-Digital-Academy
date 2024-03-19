roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 500: 'D', 900: 'CM', 1000: 'M'}

number = int(input('Enter an integer : \n'))
roman_num = ''
for key in sorted(roman_dict.keys(), reverse=True): # Sorting keys in descending order
    while number >= key:
        roman_num += roman_dict[key]
        number -= key
    if number == 0:
        break
print(f'Roman Number = {roman_num}')

input()