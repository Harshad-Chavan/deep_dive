from typing import List
#
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         sorted_list = sorted(strs, key=len)
#         smallest_string = sorted_list[0]
#         while smallest_string != "":
#             check_list = []
#             for _ in strs:
#                 check_list.append(abs(_.find(smallest_string)))
#
#             if sum(check_list) == 0:
#                 return smallest_string
#             else:
#                 smallest_string = smallest_string[0:-1]
#         return ""
#
# obj = Solution()
# print(obj.longestCommonPrefix(["flower","flow","flight"]))
# print(obj.longestCommonPrefix(["dog","racecar","car"]))
#
#
# str1 = set('harshad')
# str2 = set('sd')
#
# common_elements = str1.intersection(str2)
# print(common_elements)
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         multiplier = 1
#         end_value = 0
#         for _ in digits[::-1]:
#             end_value += _ * multiplier
#             multiplier *= 10
#         end_value += 1
#         return [int(digit) for digit in str(end_value)]
#
#
# print(Solution().plusOne(digits=[1,2,3]))


class Solution:
    def isHappy(self, n: int) -> bool:
        # code to split the number
        result_set = set()
        while n != 1:
            n = sum([int(_)**2 for _ in str(n)])
            if n in result_set:
                return False
            result_set.add(n)
        return True

print(Solution().isHappy(2))