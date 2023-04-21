
def process_input():
    n, m, d = list(map(int, input().strip().split()))
    d -= 1
    c = list(map(int, input().strip().split()))
    sum_c = sum(c)

    return n, m, d, c, sum_c


if __name__ == '__main__':
    n, m, d, c, sum_c = process_input()
    max_possible_len = d * (m + 1) + sum_c
    
    if max_possible_len < n:
        print('NO')
        exit(0)
    
    
    jumps_length = n - sum_c

    if d > 0:
        min_jumps = jumps_length // d
        smallest_jump = jumps_length % d
    else:
        min_jumps = 0
        smallest_jump = 0

    if smallest_jump != 0:
        min_jumps += 1

    result = []
    bridge_cnt = 0
    while min_jumps > 0:
        if (min_jumps == 1) and (smallest_jump != 0):
            jumping_size = [0] * smallest_jump
        else:
            jumping_size = [0] * d

        result.extend(jumping_size)
        if bridge_cnt < m:
            platform_needed = [bridge_cnt + 1] * c[bridge_cnt]
            result.extend(platform_needed)
            bridge_cnt += 1
        min_jumps -= 1

    while bridge_cnt < m:
        platform_needed = [bridge_cnt + 1] * c[bridge_cnt]
        result.extend(platform_needed)
        bridge_cnt += 1

    print("YES")
    print(" ".join(map(str, result)))
