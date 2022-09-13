n, m = input('give').split()
my_dic = {}
for a in range(int(m)):  # graph created
    lis = input().split()
    print(lis)
    if lis[0] in my_dic.keys():
        my_dic[lis[0]].append(lis[-1])
    else:
        my_dic[lis[0]] = lis[1::]
start = input()  # start node
visited = {}
for a in range(1, int(n)+1):
    visited[a] = False
print(my_dic)
