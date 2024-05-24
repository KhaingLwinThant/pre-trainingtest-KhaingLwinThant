def char_frequency(user_input):
    frequency_dict = {}
    for char in user_input:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict

user_input = input('Enter a string: ')
result = char_frequency(user_input)
print(f'Output: {result}')
