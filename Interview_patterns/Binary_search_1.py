# Find the first True in a sorted Boolean array


input_arr = [False, False, False, False, True, True, True]

def find_boundary(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


# You are given an ascending sorted array that is rotated at an unknown pivot.
# Return the minimum element in the array.
# 📌 Assume:
#
# All elements are unique
#
# Time complexity must be O(log n)
#
# Input: nums = [3, 4, 5, 1, 2]
# Output: 1
#
# Input: nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
#
# Input: nums = [11, 13, 15, 17]
# Output: 11

def find_minimum_from_the_array():
    nums = [4, 5, 6, 7, 1, 2]

    left, right = 0, len(nums) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= nums[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return nums[boundary_index]


if __name__ == "__main__":
    find_boundary(input_arr)
    print(find_minimum_from_the_array())