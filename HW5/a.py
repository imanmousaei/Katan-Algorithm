verbose = False


def printt(*values):
    if verbose:
        print(*values)


def process_input():
    n = int(input())
    s = input()

    return n, s


if __name__ == '__main__':
    t = int(input())

    for tt in range(t):
        n, s = process_input()
        sum = 0
        all_sums = [0]

        for i in range(n):
            if (s[i] == '('):
                sum += 1
            else:
                sum -= 1

            all_sums.append(sum)

        all_sums = sorted(all_sums)

        res = 0
        ns = 0
        for i in range(n+1):
            res += i*all_sums[i]-ns  # |L-R|
            res += i*(n-i+1)  # L+R
            ns += all_sums[i]

        res /= 2

        stack = []
        for i in range(n):
            if (s[i] == '('):
                stack.append(i)
            else:
                if (len(stack) == 0):
                    continue

                top = stack.pop()
                res -= (top+1)*(n-i)  # X

        print(int(res))
