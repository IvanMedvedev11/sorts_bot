def bubble_sort(numbers):
    unordered = True
    n = len(numbers)
    while unordered:
        unordered = False
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                unordered = True
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n -= 1
    return numbers
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array

