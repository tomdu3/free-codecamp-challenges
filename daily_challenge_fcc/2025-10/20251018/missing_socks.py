def sock_pairs(pairs, cycles):

    socks = pairs * 2

    wash = {
        2: -1,
        3: 1,
        4: -1,
        10: 2,
    }

    for cycle in range(1,cycles + 1):
        # Losing a sock every 2 cycles
        if cycle % 2 == 0:
            socks -= 1
        # Finding a missing sock every 3 cycles
        if cycle % 3 == 0:
            socks += 1
        # Wearing out a sock every 5 cycles
        if cycle % 5 == 0:
            socks -= 1
        # Buying a pair of socks every 10 cycles
        if cycle % 10 == 0:
            socks += 2
        # Total socks don't go below zero
        if socks < 0:
            socks = 0


    return socks // 2