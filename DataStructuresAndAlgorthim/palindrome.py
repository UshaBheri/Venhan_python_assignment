def isPalindrome(string):
    reverse_str = ""
    for char in string:
        reverse_str = char + reverse_str
    if(reverse_str == string):
        return 'Palindrome'
    else:
        return 'Not a Palindrome'

string = 'radar'
print(isPalindrome(string)) # output: Palindrome