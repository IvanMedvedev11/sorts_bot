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
