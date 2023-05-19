
def process_input():
    n = int(input())
    x = list(map(int, input().strip().split()))
    q = int(input())
    m = list(map(int, input().strip().split()))

    return n, x, q, m


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
    n, x, q, m = process_input()


    ans = binary_search(l_sorted)
    print(ans)
