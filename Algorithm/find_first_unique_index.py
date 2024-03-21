def first_unique_index(arr):
    element_count = {}
    
    # Count the occurrence of each element
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
            
    # Find the index of the first unique element
    for index, num in enumerate(arr):
        if element_count[num] == 1:
            return index
        
    return -1  # return -1 if there are no unique elements

# Test the function
arr = [3, 3, 1, 2, 4, 2]
print(first_unique_index(arr))  # Output: 2

arr = [1, 3, 1, 2, 4, 2]
print(first_unique_index(arr))  # output: 1