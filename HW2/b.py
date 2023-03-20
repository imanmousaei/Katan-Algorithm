# 1734F
dp = {}

def process_input():
    first_line = list(map(int,input().strip().split()))
    n, m = first_line
    return n, m

def decimal_to_binary(decimal):
    binary = bin(int(decimal))[2:] # convert to binary and remove "0b" prefix
    return str(binary)

# count of 1's in binary representation of n
def one_count_in_binary(n):
    binary = decimal_to_binary(n)
    return binary.count('1')

def solve(n, m):
    if m == 0:
        return 0
    if m == 1:
        one_count = one_count_in_binary(n)
        return one_count & 1
    
    if m % 2 == 1:
        t = solve(n, m - 1)
        last_steps_XOR = (m - 1) ^ (n + m - 1)
        x = one_count_in_binary(last_steps_XOR) & 1
        # print(t, x, last_steps_XOR)
        return t + x
    
    if (n, m) in dp:
        return dp[(n, m)]
    
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
    dp[(n, m)] = res
    return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        dp.clear()
        n, m = process_input()
        ans = solve(n, m)
        print(ans)
