# 1285D

def process_input():
    n = int(input())
    a = list(map(int,input().strip().split()))
    return n, a

def decimal_to_binary(decimal):
    binary = bin(int(decimal))[2:] # convert to binary and remove "0b" prefix
    return binary


def solve_for_kth_bit(arr, k):
    if k < 0:
        return 0
    # print(k)
    
    ones = []
    zeros = []
    for a in arr:
        if ((a >> k) & 1) == 1: 
            # kth bit is 1
            ones.append(a)
        else:
            zeros.append(a)
    
    # print(ones, zeros)

    if len(ones) == 0:
        return solve_for_kth_bit(zeros, k-1)
    if len(zeros) == 0:
        return solve_for_kth_bit(ones, k-1)
    
    s1 = solve_for_kth_bit(ones, k-1)
    s2 = solve_for_kth_bit(zeros, k-1)

    kth_bit = (1<<k)
    mn = min(s1, s2)
    return mn | kth_bit

if __name__ == '__main__':
    n, arr = process_input()

    k = len(decimal_to_binary(max(arr)))  # Position of the last bit in max num
    mx = solve_for_kth_bit(arr, 30)

    print(mx)
