def process_input():
    w, b, r = list(map(int, input().strip().split()))

    return w, b, r


verbose = False


def printt(*values):
    if verbose:
        print(*values)


if __name__ == '__main__':
    w, b, r = process_input()

    cnt = 0
    colors = [w, b, r]

    while (sum(colors) > 0):
        colors = sorted(colors, key=lambda x: -x)
        printt(colors)

        x, y, z = colors
        dif = min(x/2, y, x-y, y-z, (x-z)/2)
        dif = int(dif)

        if x >= 2 and y >= 1:
            dif = max(1, dif)

        # forming dif shelves of xxy
        cnt += dif
        colors[0] -= 2*dif
        colors[1] -= dif
        # print(f'dif = {dif}, x = {x}')

        if dif == 0:
            # forming dif shelves of xyz
            dif = min(colors)
            printt('dif = 0, new dif = ', dif)
            cnt += dif
            colors[0] -= dif
            colors[1] -= dif
            colors[2] -= dif
            break

    print(cnt)
