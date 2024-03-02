nums = list(map(int, input().split(" ")))


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i
        while j > 0 and elements[j - 1] > elements[j]:
            swap(elements, j, j - 1)
            j = j - 1


insertion_sort(nums)
print(nums)
