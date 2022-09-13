from cmath import inf


ar = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
stu = 7
ar.sort()
print(len(ar))
diff = 0
ind = 0
min_diff = +inf
for a in range(0, len(ar)-(stu-1)):
    diff = ar[a+6]-ar[a]
    if diff < min_diff:
        min_diff = diff
        ind = a
print(ar)
print(a)  # packets from a to a+6 are taken
