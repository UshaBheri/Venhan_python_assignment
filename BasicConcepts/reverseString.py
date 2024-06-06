def reverseString(string):
    new_str = ""
    for char in string:
        new_str = char + new_str 
    return new_str

string = "Reverse a string"
print(reverseString(string)) #output: gnirts a esreveR