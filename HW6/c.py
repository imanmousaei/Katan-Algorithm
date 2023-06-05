verbose = False

def printt(*values):
    if verbose:
        print(*values)


if __name__ == '__main__':
    t = int(input())

    for tt in range(t):
        d = 0
        s = input()
        # s = s[:-1]
        n = len(s)
        printt(f's = {s[-1]}, n = {n}')

        s = 'R' + s + 'R'
        lastR = 0

        for i in range(1, n+2):
            if (s[i] == 'R'):
                d = max(d, i - lastR)
                lastR = i

        print(d)
