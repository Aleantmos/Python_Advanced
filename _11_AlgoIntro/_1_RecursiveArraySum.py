def rec_sum(i, elements):
    if i >= len(elements):
        return 0
    amount = elements[i] + rec_sum(i + 1, elements)
    return amount


nums = list(map(int, input().split(" ")))
print(rec_sum(0, nums))
