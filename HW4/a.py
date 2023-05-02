
def process_input():
    n, m = list(map(int, input().strip().split()))
    l = []
    r = []
    
    for i in range(n):
        ll, rr = list(map(int, input().strip().split()))
        l.append(ll)
        r.append(rr)

    return n, m, l, r


if __name__ == '__main__':
    n, m, l, r = process_input()
    # get the min l of (n/2) elements for the first half. and max r of the 2nd half
