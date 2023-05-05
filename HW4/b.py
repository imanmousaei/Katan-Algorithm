def process_input():
    w, b, r = list(map(int, input().strip().split()))

    return w, b, r


if __name__ == '__main__':
    w, b, r = process_input()

    cnt = 0
    colors = [w, b, r]
    
    while (sum(colors) > 0):
        colors = sorted(colors, key=lambda x: -x)
        
        x, y, z = colors
        dif = min(x-y, y-z, (x-z)/2)
        dif = int(dif)

        # forming dif shelves of xxy
        cnt += dif
        # print('dif = ', dif)
        colors[0] -= 2*dif
        colors[1] -= dif

        if dif == 0:
            # forming dif shelves of xyz
            dif = min(colors)
            # print('dif = 0, new dif = ', dif)
            cnt += dif
            colors[0] -= dif
            colors[1] -= dif
            colors[2] -= dif
            break

    print(cnt)
