# Problem Statement:
# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase and
# removing all non-alphanumeric characters, it reads the same forward and backward.
#
# Write a function that returns true if the input string is a palindrome; otherwise, return false.
#
# Function Signature:
#
# def isPalindrome(s: str) -> bool:
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: True
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: "race a car"
# Output: False
# Constraints:
#
# 0 <= len(s) <= 2 * 10^5
#
# Only ASCII characters


def main():
    temp = "  A man, a plan, a canal: Pana"

    left  = 0
    right = len(temp) - 1

    while left < right:
        while left < right and not temp[left].isalnum():
            left += 1

        while left < right and not temp[right].isalnum():
            right -= 1

        if not temp[left].lower() == temp[right].lower():
            result = False
            break
        else:
            left += 1
            right -= 1
    else:
        result = True

    print(result)






if __name__ == "__main__":
    main()