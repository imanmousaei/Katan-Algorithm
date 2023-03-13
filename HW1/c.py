n = 0
visited = []
adj = [[]]


def process_input():
    global visited, adj, n
    n = int(input())
    visited = [False for _ in range(n+1)]
    adj = [[] for _ in range(n+1)]

    c = n*(n-1) // 2

    for i in range(c):
        id1, id2, fr, sc = list(input().strip().split())
        id1, id2 = int(id1), int(id2)
        if fr == '+' and sc == '+':
            adj[id1].append(id2)
            adj[id2].append(id1)
            # print(id1, id2)


def find_max_clique():
    global visited, adj, n
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        cnt = dfs(i)
        # print(f'cnt[{i}] = {cnt}')
        # print(f'visited = {visited}')
        if cnt > n/2:
            return i

def dfs(idx, count=1):
    global adj, visited
    cnt = count
    visited[idx] = True
    # print(f'idx = {idx}, count = {count}')
    # print(adj)

    for neighbor in adj[idx]:
        if not visited[neighbor]:
            # print(f'idx = {idx}, neighbor = {neighbor}, count = {count}')
            cnt = max(cnt, dfs(neighbor, count+1))
    return cnt

def print_visited(idx):
    global visited
    visited = [False for _ in range(n+1)]
    dfs(idx)

    ans = ""
    for i in range(1, n+1):
        if visited[i] == True:
            ans += "+"
        else:
            ans += "-"
    print(ans)

if __name__ == '__main__':
    process_input()
    idx = find_max_clique()
    # print(f'idx = {idx}')
    print_visited(idx)
