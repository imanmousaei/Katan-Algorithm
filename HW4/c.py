import heapq


def process_input():
    n = int(input())
    a = []
    b = []
    hp = []
    heapq.heapify(hp)
    
    for i in range(n):
        aa, bb = list(map(int, input().strip().split()))
        a.append(aa)
        b.append(bb)
        heapq.heappush(hp,  (aa,bb,i) )

    return n, a, b, hp


if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        n, a, b, hp = process_input()
