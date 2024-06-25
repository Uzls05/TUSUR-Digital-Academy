def largest_histogram(histogram):
    stack = []
    max_area = 0
    index = 0

    while index < len(histogram):
        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, histogram[top_of_stack] * width)

    while stack:
        top_of_stack = stack.pop()
        width = index if not stack else len(histogram) - stack[-1] - 1
        max_area = max(max_area, histogram[top_of_stack] * width)

    return max_area


print(largest_histogram([5]))
print(largest_histogram([5, 3]))
print(largest_histogram([1, 1, 4, 1]))
print(largest_histogram([1, 1, 3, 1]))
print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))

