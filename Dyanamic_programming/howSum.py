targetSum = 7
numbers = [5, 3, 4, 7]
res = []


def howSum(targetSum, numbers):
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:

        remainder = targetSum - num
        print(f"calling Function with {remainder}-{num}")
        arr = howSum(remainder, numbers)
        if arr is not None:
            arr.insert(0,num)
            return arr


    return None

print(howSum(targetSum, numbers))
