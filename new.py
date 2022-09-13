print('hello')
# search in rotated sorted array


target = 3
nums = [4, 5, 6, 7, 0, 1, 2]


def fun(nums, t):
    l, r = 0, len(nums)-1
    if len(nums) == 1 and nums[0] == target:
        return 0
    elif len(nums) == 1 and nums[0] != target:
        return -1
    else:
        while r >= l:
            mid = (l+r)//2
            if nums[mid] == target:

                return mid
            if nums[mid] < nums[r]:  # right sorted
                if (target > nums[mid]) and (target <= nums[r]):
                    l = mid+1
                else:
                    r = mid-1

            else:
                if (target >= nums[l]) and (target < nums[mid]):
                    r = mid-1
                else:
                    l = mid+1

        return -1


a = fun(nums, 3)
print(a)
print('hello')
