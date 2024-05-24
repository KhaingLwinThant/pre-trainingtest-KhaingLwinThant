def ispalindrome(user_input):
    str = ''.join(char for char in user_input if char.isalnum()).lower()
    return str == str[ : : -1]
        
while True:
    user_input = input('Enter a string: ')
    if ispalindrome(user_input):
        print('The string is a palindrome.')
    else:
        print('The string is not a palindrome.')
    
    restart = input('Do you want to continue? y/n: ').lower()
    if restart == 'no':
        break
