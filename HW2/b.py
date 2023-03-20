# 1734F

def process_input():
    first_line = list(map(int,input().strip().split()))
    n, m = first_line
    return n, m

def decimal_to_binary(decimal):
    binary = bin(int(decimal))[2:] # convert to binary and remove "0b" prefix
    return str(binary)

cache = {}

# count of 1's in binary representation of n
def popcount(n):
    binary = decimal_to_binary(n)
    return binary.count('1')
    # res = 0
    # while n:
    #     res += 1
    #     n &= n - 1
    # return res

def solve(n, m):
    if m == 0:
        return 0
    if m == 1:
        return popcount(n) & 1
    
    if m % 2 == 1:
        t = solve(n, m - 1)
        x = popcount((m - 1) ^ (n + m - 1)) & 1
        # print(t, x)
        return t + x
    if (n, m) in cache:
        return cache[(n, m)]
    
    if n % 2 == 0:
        one_cell = 2
        zero_cell = 0
        cnt1 = solve(n // 2, m // 2)
        cnt0 = m // 2 - cnt1
    else:
        one_cell = 0
        zero_cell = 1
        cnt1 = solve(n // 2, m // 2) + solve(n // 2 + 1, m // 2)
        cnt0 = m - cnt1
    res = one_cell * cnt1 + zero_cell * cnt0
    # print(f'n = {n}, m = {m}, cnt1 = {cnt1}, cnt0 = {cnt0}, one_cell = {one_cell}, zero_cell = {zero_cell}')
    cache[(n, m)] = res
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        cache.clear()
        n, m = process_input()
        ans = solve(n, m)
        print(ans)
