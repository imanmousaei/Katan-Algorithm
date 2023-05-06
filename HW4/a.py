
def process_input():
    n, s = list(map(int, input().strip().split()))
    l = []
    r = []
    all = []

    for i in range(n):
        ll, rr = list(map(int, input().strip().split()))
        l.append(ll)
        r.append(rr)
        all.append((ll, rr, i))

    return n, s, l, r, all


def check(l_sorted, x):
    ans = 0
    cnt = 0
    for val in l_sorted:
        if (val[0] > x):
            cnt += 1
        elif (val[1] >= x):
            ans += x - val[0]
            cnt += 1
        if (cnt == (n+1)/2):
            break

    if (cnt < (n+1)/2):
        return False
    if (ans > s):
        return False
    return True

def binary_search(l_sorted):
    low = 1
    high = 1e14
    while low != high:
        mid = (high + low + 1) // 2

        if (check(l_sorted, mid)):
            low = mid
        else:
            high = mid-1
    
    return int(low)


if __name__ == '__main__':
    n, s, l, r, all = process_input()
    # get the min l of half elements for the first half. and max r of the 2nd half
    l_sorted = sorted(all, key=lambda x: -x[0])
    # print(l_sorted)

    s -= sum(l)

    ans = binary_search(l_sorted)
    print(ans)
