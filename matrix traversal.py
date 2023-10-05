# Python3 program showing time difference
# in row major and column major access

# taking MAX 10000 so that time difference
# can be shown
from time import perf_counter

MAX = 5

arr = [[i for i in range(MAX)] for i in range(MAX)]


def rowMajor():
    global arr

    # accessing element row wise
    for i in range(MAX):
        for j in range(MAX):
            arr[i][j] += 1


def colMajor():
    global arr

    # accessing element column wise
    for i in range(MAX):
        for j in range(MAX):
            arr[j][i] += 1


# Driver code
if __name__ == '__main__':
    # Time taken by row major order
    t = perf_counter()
    rowMajor()
    t = perf_counter() - t
    print("Row major access time :{:.2f} s".format(t))

    # Time taken by column major order
    t = perf_counter()
    colMajor()
    t = perf_counter() - t
    print("Column major access time :{:.2f} s".format(t))

# This code is contributed by mohit kumar 29
