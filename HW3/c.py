

def process_input():
    n, m, d = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))

    return n, m, d, c


def fill_with_num(arr, num, start, end):
    for i in range(start, end+1):
        # print(i)
        arr[i] = num
    return arr


if __name__ == '__main__':
    n, m, d, c = process_input()

    current = 0
    bridges = [-1]
    possible = True
    ans = [0]*n
    while current < n+1:
        print(current, d)
        last_bridge = bridges[-1]
        current_bridge = last_bridge + 1

        if last_bridge+1 < m:
            bridges.append(current_bridge)
        else:
            possible = False
            break

        print(current + d, current+d+c[current_bridge])
        ans = fill_with_num(ans, current_bridge, current +
                            d, current+d+c[current_bridge])
        print(ans)
        current += d + c[current_bridge]

    if possible:
        print('YES')
        print(ans)
    else:
        print('NO')
