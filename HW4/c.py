import heapq


def process_input():
    n = int(input())
    a = []
    b = []
    hp = []
    tanks = []
    
    for i in range(n):
        aa, bb = list(map(int, input().strip().split()))
        a.append(aa)
        b.append(bb)
        tanks.append(  (aa,bb,i) )

    return n, a, b, tanks


if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        n, a, b, tanks = process_input()
