import numpy as np


def process_input():
    first_line = list(map(int,input().strip().split()))
    n, d = first_line
    return n, d

def find_min_diff(a, l, r):
    sr = sorted(a[l:r+1])

    min_diff = np.inf
    for i in range(1, len(sr)):
        min_diff = min(sr[i] - sr[i-1], min_diff)

    return min_diff


if __name__ == '__main__':
    n, d = process_input()
    a = list(map(int,input().strip().split()))

    ans = []

    for i in range(d):
        l, r = process_input()
        
        min_diff = find_min_diff(a, l-1, r-1)

        ans.append(min_diff)

    for answer in ans:
        print(answer)