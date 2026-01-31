target_sum = 7
numbers = [1,3,2,2]

def bestSum(target_sum, numbers , combination=[]):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = bestSum(remainder, numbers, combination)
        if remainder_combination is not None:
            remainder_combination.append(num)
            if  shortest_combination is None or len(remainder_combination) < len(shortest_combination):
                shortest_combination = remainder_combination

    return shortest_combination

print(bestSum(target_sum, numbers))
