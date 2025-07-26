# Given a string s, find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: 3  # "abc"
#
# Input: "bbbbb"
# Output: 1  # "b"
#
# Input: "pwwkew"
# Output: 3  # "wke"

from collections import defaultdict

def longest_substring(s):
    longest = 0
    l = 0

    counter = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]] += 1

        # To check if character is repeating
        while counter[s[r]] > 1:
            # if character repeats
            counter[s[r]] -= 1
            # move left pointer ahead
            l += 1
        # check longest
        longest = max(longest, r - l + 1)
    return longest

if __name__ == "__main__":
    print(longest_substring("abcabcbb"))
