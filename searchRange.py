import ast
def searchRange(nums, target):
    left = 0
    right = len(nums)-1
    index_lst = [-1,-1]
    if len(nums) == 0:
        return index_lst
    if target not in nums:
        return index_lst   
    while left <= right:
        m = left + (right-left)//2
        if nums[m] == target:
            break
        elif nums[m] < target:
            left = m + 1
        else:
            right = m -1
    l = r = m
    while l>= 0 and target == nums[l]:
        index_lst[0] = l
        l-=1
    while r<=len(nums)-1 and target == nums[r]:
        index_lst[1] = r
        r+=1
    return index_lst    

if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    target = int(input("Enter the target = "))
    res = searchRange(input_lst, target)
    print(res)
