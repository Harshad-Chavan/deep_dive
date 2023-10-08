arr = [14, 2, -4, -20, 10]


def subarray(arr, target_value):
    _dict = {}
    current_sum = 0

    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if current_sum == target_value:
            print("subarray starts from 0 to ", i)
            break
        diff = current_sum - target_value
        if diff in _dict:
            print(_dict[diff] + 1, "&", i)
            break
        _dict[current_sum] = i


subarray(arr, -24)
