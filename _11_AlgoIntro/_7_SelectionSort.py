nums = list(map(int, input().split(" ")))


def swap(elements, i, min):
    temp = elements[i]
    elements[i] = elements[min]
    elements[min] = temp


def sort(elements):
    size = len(elements)
    for i in range(size):
        min = i

        for j in range(i + 1, size):
            if elements[j] < elements[min]:
                min = j

        swap(elements, i, min)


sort(nums)
print(nums)
