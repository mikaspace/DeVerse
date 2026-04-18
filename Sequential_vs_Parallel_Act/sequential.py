def merge(left, right):
    result = []
    a = j = 0

    while a < len(left) and j < len(right):
        if left[a] <= right[j]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[a:])
    result.extend(right[j:])
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

