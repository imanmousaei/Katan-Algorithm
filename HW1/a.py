def process_input():
    first_line = list(map(int,input().strip().split()))
    n, t = first_line
    a = list(map(int,input().strip().split()))
    return n, t, a

def solve(n, t, a):
    cnt, overall_sum = 0, 0

    for right in range(0, n):
        left = 0
        overall_sum += a[right]

        sum = overall_sum
        for left in range(0, right+1):
            if sum < t:
                cnt += 1

            sum -= a[left]

    return cnt

if __name__ == '__main__':
    n, t, a = process_input()
    cnt = solve(n, t, a)
    print(cnt)
