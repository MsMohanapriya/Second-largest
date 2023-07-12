def second_largest(array):
    if len(array) <= 1:
        return "Array has only one element"

    max_val = float('-inf')
    second_max = float('-inf')

    for num in array:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num < max_val:
            second_max = num

    if second_max == float('-inf'):
        return "No second largest element found"
    else:
        return second_max

array = list(map(int, input().split()))
print(second_largest(array))
