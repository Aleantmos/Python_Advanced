def searching(searched, nums):
    def binary_search(start, end, i):
        curr = nums[i]

        if curr == searched:
            return i
        elif searched < curr:
            end = i - 1
        elif searched > curr:
            start = i + 1

        i = (start + end) // 2
        return binary_search(start, end, i)

    s, e = 0, len(nums) - 1
    mid = len(nums) // 2
    print(binary_search(s, e, mid))


nums = list(map(int, input().split(" ")))
searched = int(input())

searching(searched, nums)
