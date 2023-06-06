verbose = False
# verbose = True


def printt(*values):
    if verbose:
        print(*values)


def process_input():
    n = int(input())
    g = [0] * n
    for i in range(n):
        g[i] = list(map(int, input().strip().split()))

    tr = list(map(int, input().strip().split()))
    tr = [x-1 for x in tr]  # convert to 0-based
    return n, g, tr


if __name__ == '__main__':
    n, g, tr = process_input()
    ans = [0] * (n+2)

    for cur in range(n-1, -1, -1):
        printt('cur: ', cur)
        what = tr[cur]
        for i in range(n):
            for j in range(n):
                x = tr[i]
                y = tr[j]
                # printt('xy = ', x, y)
                g[x][y] = min(g[x][y], g[x][what] + g[what][y])
        
        printt(g)

        for i in range(cur, n):
            for j in range(cur, n):
                ans[cur] += g[tr[i]][tr[j]]

    for i in range(n):
        print(ans[i], end=' ')
    print()
