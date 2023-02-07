def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp






nums = [23,24,56,12,21,56,34,11]

sort(nums)

print(nums)