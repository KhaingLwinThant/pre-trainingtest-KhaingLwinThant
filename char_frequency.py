user_input = input('Enter a string: ')
char_frequency = {}
for i in user_input:
    char_frequency[i] = user_input.count(i)

print(f'Output: {char_frequency}')
