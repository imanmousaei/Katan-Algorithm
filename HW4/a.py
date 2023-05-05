
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


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    n, s, l, r, all = process_input()
    # get the min l of half elements for the first half. and max r of the 2nd half
    l_sorted = sorted(all, key=lambda x: x[0])
    print(l_sorted)
    
    if n & 1:
        middle = (n+1)/2
    else:
        middle = n/2
    
    middle = int(middle)
    print(middle)
        
    result = [x[0] for x in l_sorted[:middle-1]]
    s -= sum(result)
    print(result, s)
    
    each = s / (n - middle + 1)
    print(each)
    
        
    
