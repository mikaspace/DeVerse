def merge_lists(left_part, right_part):
    merged = []
    l_idx = r_idx = 0

    while l_idx < len(left_part) and r_idx < len(right_part):
        if left_part[l_idx] <= right_part[r_idx]:
            merged.append(left_part[l_idx])
            l_idx += 1
        else:
            merged.append(right_part[r_idx])
            r_idx += 1

    merged.extend(left_part[l_idx:])
    merged.extend(right_part[r_idx:])
    return merged


def divide_and_merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left_part = divide_and_merge_sort(values[:mid])
    right_part = divide_and_merge_sort(values[mid:])
    return merge_lists(left_part, right_part)