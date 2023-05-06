import heapq


def process_input():
    n = int(input())
    a = []
    b = []
    hp = []
    tanks = []

    for i in range(n):
        aa, bb = list(map(int, input().strip().split()))
        a.append(aa)
        b.append(bb)
        tanks.append((aa, bb, i))

    return n, a, b, tanks

verbose = True
def printt(*values):
    if verbose:
        print(*values)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        n, a, b, tanks = process_input()

        tanks = sorted(tanks, key=lambda x: (x[0], -x[1])) # least a with most b
        printt(tanks)

        idx = tanks[0][2]
        cnt = 0
        rockets = a[idx]
        printt(f'rockets = {rockets}')

        while cnt < n-1:
            printt('idx = ', idx)
            cnt += 1
            last_idx = idx
            idx = (idx+1) % n

            a[idx] -= b[last_idx]
            if a[idx] < 0:
                a[idx] = 0

            rockets += a[idx]
            printt(f'a = {a[idx]}, rockets = {rockets}')

        print(rockets)
