import heapq


def process_input():
    n = int(input())
    x = list(map(int, input().strip().split()))
    q = int(input())

    return n, x, q


def printt(*values):
    if verbose:
        print(*values)


def find_max(arr, key):
    mx = float('-inf')

    for val in arr:
        if val > mx:
            mx = val

    return val


if __name__ == '__main__':
    verbose = False

    n, x, q = process_input()

    mx = max(x)
    cnt = [0]*(mx+1)
    dp = [0]*(mx+1)

    for i, val in enumerate(x):
        cnt[val] += 1

    # dp[i] = ( cnt adade <= i )
    dp[0] = cnt[0]
    for i in range(1, mx+1):
        dp[i] = dp[i-1] + cnt[i]

    for i in range(q):
        m = int(input())
        if (m >= mx):
            print(n)
        else:
            print(dp[m])
