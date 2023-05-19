def process_input():
    n = int(input())
    a = list(map(int, input().strip().split()))

    return n, a


verbose = False


def printt(*values):
    if verbose:
        print(*values)


if __name__ == '__main__':
    t = int(input())

    for tt in range(t):
        n, a = process_input()

        res = 0
        mx = 0
        s = 0
        for i in range(n):
            mx = max(mx, a[i])
            s ^= a[i]
            res = max(res, (s ^ mx))

        for i in range(n):
            mx = 0
            s = 0

            tah = n
            
            for j in range(i, tah):
                mx = max(mx, a[j])
                s ^= a[j]
                res = max(res, (s ^ mx))

        print(res)
