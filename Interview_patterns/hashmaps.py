# Problem:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# Example:
#
# python
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]  # Because nums[0] + nums[1] = 2 + 7 = 9


# worst case : no element found o(n)

def main():
    nums = [2,7,11,15]
    target = 17
    result = []


    num_to_index = dict()

    for index,num in enumerate(nums):
        diff = target - num
        if diff in num_to_index:
            result.append(num_to_index[diff])
            result.append(index)
        else:
            num_to_index[num] = index

    print(result)


if __name__ == "__main__":
    main()