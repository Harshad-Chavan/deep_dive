memo = {}
def grid_travelar(m,n):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[(m,n)] = grid_travelar(m-1,n) + grid_travelar(m,n-1)
    return memo[(m,n)]


print(grid_travelar(18,18))