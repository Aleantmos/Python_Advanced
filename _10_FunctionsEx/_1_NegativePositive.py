def find_total(nums_str):
    positives = []
    negatives = []

    def separate():
        nums = map(int, nums_str.split(" "))
        for el in nums:
            if el > 0:
                positives.append(el)
            else:
                negatives.append(el)

    def sum_numbers(numbers):
        result = 0
        for el in numbers:
            result += el
        return result

    def get_result():
        result = ""

        def find_difference():
            nonlocal result

            positive_res = sum_numbers(positives)
            result += str(positive_res) + "\n"

            negative_res = sum_numbers(negatives)
            result += str(negative_res) + "\n"
            return positive_res - negative_res

        diff = find_difference()

        if diff > 0:
            result += str("The positives are stronger than the negatives")
        else:
            result += str("The negatives are stronger than the positives")

        return result

    separate()
    return get_result()


str_input = input()

print(find_total(str_input))
