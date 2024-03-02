nums = list(map(int, input().split(" ")))


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def bubble_sort(nums):
    size = len(nums)
    for i in range(1, size):
        for j in range(0, size - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)


bubble_sort(nums)
print(nums)
