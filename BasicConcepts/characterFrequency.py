def characterFrequency(string):
    frequency_dict = {}
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

string = "Frequency of characters"
print(characterFrequency(string))

# output: {'F': 1, 'r': 3, 'e': 3, 'q': 1, 'u': 1, 'n': 1, 'c': 3, 'y': 1, ' ': 2, 'o': 1, 'f': 1, 'h': 1, 'a': 2, 't': 1, 's': 1}