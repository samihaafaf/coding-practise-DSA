from ast import Store


f = open('new.txt')
#n = f.read()
n = f.readline()
arr = f.readline().split()
#print(n, end='')
# print(arr)

# print(n)


for i in range(len(arr)):
    arr[i] = int(arr[i])


def min_dis(arr):
    mini = len(arr)

    for i in range(len(arr)):
        store = 0
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                store = abs(j-i)
                if store < mini:
                    mini = store
    if mini == int(n):
        print(-1)
    else:
        print(mini)


min_dis(arr)


f.close()
