
from pickle import FALSE

cases = int(input())


def my():
    st = int(input())
    arr = input().split()

    def sum(ar, ind):
        if ind == 0:
            return int(ar[ind])
        else:
            return int(ar[ind]) + sum(ar, ind-1)

    for a in range(st):
        flag = FALSE
        ar1 = arr[:a]
        sum1, sum2 = 0, 0

        ar2 = arr[a+1:]
        if not ar1:  # ar1 is empty
            lis = list(filter(lambda each: each != '0', ar2))
            if len(lis) == 0:
                flag = True
                break
        elif not ar2:
            lis = list(filter(lambda each: each != '0', ar1))
            if len(lis) == 0:
                flag == True
                break
        elif len(list(filter(lambda each: each != '0', ar1))) == 0 and len(list(filter(lambda each: each != '0', ar2))) == 0:
            flag = True
            break
        else:
            sum1 = sum(ar1, len(ar1)-1)
            sum2 = sum(ar2, len(ar2)-1)
            if sum1 == sum2:
                flag = True
                break

    if flag == True:
        print('YES')
    else:
        print('NO')


for a in range(cases):
    my()
