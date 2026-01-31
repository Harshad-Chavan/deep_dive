targetSum = 500
numbers = [5,3,4,7]

def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder, numbers)):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(canSum(targetSum, numbers))

