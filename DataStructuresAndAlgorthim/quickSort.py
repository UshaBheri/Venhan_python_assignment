def quickSort(array):
    if(len(array) <= 1):
        return array
    
    middle_element = array[len(array)//2]
    left = []
    right = []
    middle = []

    for i in array:
        if i < middle_element:
            left.append(i)
        elif i == middle_element:
            middle.append(i)
        else:
            right.append(i)

    return quickSort(left) + middle + quickSort(right)

array = [3,6,8,7,2]
print(quickSort(array)) # output: [2, 3, 6, 7, 8]