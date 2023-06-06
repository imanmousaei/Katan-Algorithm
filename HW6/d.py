verbose = False
# verbose = True


def printt(*values):
    if verbose:
        print(*values)


def dfs(v):
    vis[v] = True
    for u in adj[v]:
        if (not vis[u]):
            dfs(u)


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))

    p = []
    maxn = 2*n + 2
    vis = [False] * maxn
    adj = []
    
    for i in range(maxn):
        adj.append([] * maxn)
    cnt = 0

    tmp = list(map(int, input().strip().split()))
    for i, value in enumerate(tmp):
        p.append((value, i))
        
    printt(adj)

    for i in range(m):
        x, y = list(map(int, input().strip().split()))
        printt(f'xy = ', x, y)
        x -= 1
        y -= 1

        adj[x].append(y)
        adj[y].append(x)
        
        printt(adj)


    # printt(p)
    # printt(adj[0])

    p.sort()

    for i in range(n):
        if (not vis[p[i][1]]):
            dfs(p[i][1])
            cnt += p[i][0]

    print(cnt)
