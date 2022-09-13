ar = [-2, 1, 3, 0, -5]


def kadanes(ar):
    if len(ar) == 1:
        return ar[0]
    else:
        maxc, gsum = ar[0], ar[0]
        for a in range(1, len(ar)):
            check = ar[a]+maxc
            if check >= ar[a]:
                maxc = check
            else:
                maxc = ar[a]
            if maxc > gsum:
                gsum = maxc
        return gsum


print(kadanes(ar))
