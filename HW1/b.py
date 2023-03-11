mn = []
mx = []

def process_input():
    first_line = list(map(int,input().strip().split()))
    n, d = first_line
    return n, d

def find_min_max(a, l, r):
    print(f'l = {l}, t = {r}')
    if mn[l][r] != 0 and mx[l][r] != 0:
        print(f'mn[{l}][{r}] = {mn[l][r]}, mx[{l}][{r}] = {mx[l][r]}')
        return mn[l][r], mx[l][r]
    
    if l == r:
        mn[l][l] = a[l]
        mx[l][l] = a[l]
        return a[l], a[l]
    
    mid = (l + r) // 2
    mn1, mx1 = find_min_max(a, l, mid)
    mn2, mx2 = find_min_max(a, mid+1, r)

    mn[l][r] = min(mn1, mn2)
    mx[l][r] = max(mx1, mx2)
    
    print(f'mn[{l}][{r}] = {mn[l][r]}, mx[{l}][{r}] = {mx[l][r]}')
    return mn[l][r], mx[l][r]


if __name__ == '__main__':
    n, d = process_input()
    a = list(map(int,input().strip().split()))
    mn = [[0]*n]*n
    mx = [[0]*n]*n
    # find_min_max(a, 0, n-1)
    ans = []

    find_min_max(a, 1, 2)

    # for i in range(d):
    #     l, r = process_input()
        
    #     lrmin, lrmax = find_min_max(a, l-1, r-1)
    #     ans.append(lrmax - lrmin)

    # for answer in ans:
    #     print(answer)