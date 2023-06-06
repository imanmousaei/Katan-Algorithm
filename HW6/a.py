verbose = False
# verbose = True


def printt(*values):
    if verbose:
        print(*values)


def process_input():
    n, m = list(map(int, input().strip().split()))
    return n, m


def BFS(v):
    q = []
    dp[v] = 0
    vis[v] = True
    q.append(v)

    while (len(q) > 0):
        v = q.pop(0)
        printt('v =', v)
        printt(dp)

        if (v >= 1):
            dp[v-1] = min(dp[v-1], dp[v] + 1)
            printt(f'dp[{v-1}] = min({dp[v-1]}, {dp[v] + 1})')
            if (not vis[v-1]):
                vis[v-1] = True
                q.append(v-1)

        if (v <= m):
            dp[2*v] = min(dp[2*v], dp[v] + 1)
            printt(f'dp[{2*v}] = min({dp[2*v]}, {dp[v] + 1})')
            if (not vis[2*v]):
                vis[2*v] = True
                q.append(2*v)


if __name__ == '__main__':
    n, m = process_input()
    # printt(n, m)
    
    maxm = 2*m + 2
    vis = [False] * maxm
    dp = [float('inf')] * maxm

    # printt(vis)
    # printt(dp)

    if (n >= m):
        print(n-m)
    else:
        BFS(n)
        printt(dp)

        print(dp[m])
