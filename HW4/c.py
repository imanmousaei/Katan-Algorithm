import heapq


def process_input():
    n = int(input())
    a = []
    b = []
    tanks = []

    for i in range(n):
        aa, bb = list(map(int, input().strip().split()))
        a.append(aa)
        b.append(bb)
        tanks.append((aa, bb, i))

    return n, a, b, tanks


def printt(*values):
    if verbose:
        print(*values)


def get_previous_index(idx):
    prev = idx - 1
    if prev == -1:
        prev = n-1
    return prev


def get_after_index(idx):
    return (idx+1) % n


def solve_for_index(idx):
    a = aa.copy()
    b = bb.copy()

    cnt = 1
    rockets = a[idx]
    printt(f'rockets = {rockets}')

    while cnt < n:
        printt('idx = ', idx)
        cnt += 1
        last_idx = idx
        idx = (idx+1) % n

        a[idx] -= b[last_idx]
        if a[idx] < 0:
            a[idx] = 0

        rockets += a[idx]
        printt(f'a = {a[idx]}, rockets = {rockets}')

    return rockets


def find_min(arr, key):
    mn = float('inf')
    idx = -1

    for i, val in enumerate(arr):
        k = key(val)
        if k < mn:
            mn = k
            idx = i
        elif k == mn and i < idx:
            idx = i

    return idx


if __name__ == '__main__':
    verbose = False

    t = int(input())
    for i in range(t):

        n, aa, bb, tanks = process_input()

        idx = find_min(tanks, key=lambda x: (x[0]-x[1]))
        rockets1 = solve_for_index(idx)

        idx = find_min(tanks, key=lambda x: (-x[0]))
        rockets2 = solve_for_index(idx)

        idx = find_min(tanks, key=lambda x: (x[1]))
        rockets3 = solve_for_index(idx)
        
        idx = find_min(tanks, key=lambda x: (x[1]))
        idx = get_after_index(idx)
        rockets4 = solve_for_index(idx)

        print(min(rockets1, rockets2, rockets3, rockets4))
