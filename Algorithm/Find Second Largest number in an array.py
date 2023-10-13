'''
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

def get_second_largest(arr):
    second_max = float("-inf")
    first_max = float("-inf")

    for i in range(0, len(arr)):
        item = int(arr[i])
        if item > first_max:
            second_max = first_max  # 原本最大的變成老二
            first_max = item
        elif item > second_max and item < first_max:
            second_max = item

    return -1 if second_max == float("-inf") else second_max

nums = [3,2,1,5,6,4]
res = get_second_largest(nums)
print(f"result:{res}")

nums = [3,2,3,1,2,4,5,5,6]
res = get_second_largest(nums)
print(f"result:{res}")