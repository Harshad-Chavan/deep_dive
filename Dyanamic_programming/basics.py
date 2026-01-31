map = {}
map.update({1:1,2:1})
def fib_num(n):
    if n in map:
        return map[n]
    map[n] = fib_num(n-1) + fib_num(n-2)
    return map[n]

print(fib_num(50))