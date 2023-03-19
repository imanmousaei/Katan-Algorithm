teams = {}

def add_team_to_dict(depth, team):
    # print(teams)
    if depth in teams:
        t = teams[depth]
        # print(t, team)
        teams[depth] = list(t) + list(team)
    else:
        teams[depth] = team

def solve(first, last, depth=0):
    if first == last:
        return teams

    mid = (first + last) // 2

    team = [i for i in range(first, mid+1)]
    add_team_to_dict(depth, team)

    solve(first, mid, depth+1)
    solve(mid+1, last, depth+1)


if __name__ == '__main__':
    n = int(input())
    solve(1, n)
    print(len(teams))
    for depth in teams:
        t = teams[depth]
        print(len(t), end=' ')
        t = set(t)
        for a in t:
            print(a, end=' ')
        print()
