# Input: exp = “[()]{}{[()()]()}”
# Output: Balanced
# Explanation: all the brackets are well-formed
#
# Input: exp = “[(])”
# Output: Not Balanced
# Explanation: 1 and 4 brackets are not balanced because
# there is a closing ‘]’ before the closing ‘(‘

import unittest as ut

input_exp_1 = "[()]{}{[()()]()}"
input_exp_2 = "])"
stack = []


def check_balance(input_exp):
    for _ in input_exp:
        if _ in ["[", "(", "{"]:
            stack.append(_)
        else:
            if not stack:
                #becoz stack is empty
                return "Unbalanced"
            if _ == "]" and stack[-1] == "[":
                stack.pop(-1)
            elif _ == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif _ == ")" and stack[-1] == "(":
                stack.pop(-1)
            else:
                return "unbalanced"
    else:
        if not len(stack):
            return "Balanced"

print(check_balance(input_exp_2))