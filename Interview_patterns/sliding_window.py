# Given an array of integers and an integer k, find the maximum sum of a subarray of size k.

# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: Subarray [5, 1, 3] has the maximum sum.


# fixed window appraoch
def one_appraoch_less_efficient():
    nums = [2, 1, 5, 1, 3, 2, 10, 0, 1, 2, 3]
    k = 3

    left = 0
    right = k

    max = 0

    while right < len(nums) + 1:
        window = nums[left:right]
        window_sum = sum(nums[left:right])
        print(f"window:{window} , sum: {window_sum}")
        if window_sum > max:
            max = window_sum
            max_window = window
        # remove one from left
        left += 1

        # add ome to right
        right += 1

    print(max, max_window)

def better_approach():
    nums = [2, 1, 5, 1, 3, 2, 10, 0, 1, 2, 3]
    k = 3
    nums_len = len(nums)

    if nums_len < k:
        print("Not enough elements")

    largest = current_sum = sum(nums[0:k])
    # print(f"{nums[0:k]} , sum:{current_sum}")
    for i in range(k,nums_len):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        print(f"{nums[i - k:i]} , sum:{sum(nums[i - k:i])}")
        largest = max(current_sum,largest)

    print(largest)








if __name__ == "__main__":
    one_appraoch_less_efficient()
    print("*"*10)
    better_approach()
