

def bin(ar, val):
    l = 0
    r = len(ar)-1
    while l <= r:
        mid = (l+r)//2
        if ar[mid] == val:
            return 'yes'
        else:
            if ar[mid] > val:
                r = mid-1
            else:
                l = mid+1


arr = [1, 2, 3, 4]
a = bin(arr, 1)
print(a)


# ar = [1, 2, 3, 4, 0, 5, 1]
# # ar.sort()  # sorting the array
# c = 0
# for a in range(len(ar)):
#     if a != (len(ar)-1) and ar[a] in ar[a+1:]:
#         c = 1
#         break
# if c == 1:
#     print('true')
# else:
#     print('false')


# bad approach

# def ch(ar):
#     if len(ar) == 1:
#         return False
#     else:
#         check = 0
#         for a in range(len(ar)):
#             if check == 1:
#                 break
#             else:
#                 val = ar[a]
#                 for b in range(a, len(ar)):
#                     if a != b:
#                         if val == ar[b]:
#                             check = 1
#                             break
#     if check == 1:
#         print('true')
#     else:
#         print('false')


# ch(ar)
