arr = [1, 2, 3, 4, 6, 7]


def find_missing_number(inp_arr):
    max_val = max(arr)
    min_val = min(arr)
    n = len(range(min_val, max_val+1))

    sum_of_given_arr = sum(arr)
    sum_of_expected_arr = int((n * (n + 1)) / 2)

    missing_number = sum_of_expected_arr - sum_of_given_arr
    if not missing_number:
        print("No Number missing")
    else:
        print(missing_number)

    return

find_missing_number(arr)