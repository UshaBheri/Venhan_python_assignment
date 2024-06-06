def duplicateElements(array):
    unique_values = {}
    count = []
    for i in array:
        if i in unique_values:
            unique_values[i] += 1
        else:
            unique_values[i] = 1
    for i,j in unique_values.items():
        if(j > 1):
            count.append(i)
    return count
    
array = [1,2,2,3,4,5,5]
print(duplicateElements(array)) # output: [2,5]