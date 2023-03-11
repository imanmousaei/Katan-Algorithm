def process_input():
    first_line = list(map(int,input().strip().split()))
    n, t = first_line
    a = list(map(int,input().strip().split()))
    return n, t, a

def solve(n, t, a):
    cnt, right_sum = 0, 0

    for right in range(0, n):
        left = 0

        right_sum += a[right]
        sum = right_sum

        while left <= right:
            if sum < t:
                cnt += 1

            sum -= a[left]
            left += 1

    return cnt

if __name__ == '__main__':
    n, t, a = process_input()
    cnt = solve(n, t, a)
    print(cnt)
