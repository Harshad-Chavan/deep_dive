from collections import Counter

input_str = "ababababacdedefgfg"
counter = Counter(input_str)

temp_list = list(input_str)
for _ in temp_list:
    if counter[_] == 1:
       print(_)

pass
