def merge_sort_string(array: list[str]):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    leftList = merge_sort_string(array[:mid])
    rightList = merge_sort_string(array[mid:])
    return merge(leftList, rightList)


def merge(left: list[str], right: list[str]):
    left_letter, right_letter = 0, 0
    merged = []

    while left_letter < len(left) and right_letter < len(right):
        if left[left_letter] <= right[right_letter]:
            merged.append(left[left_letter])
            left_letter += 1
        else:
            merged.append(right[right_letter])
            right_letter += 1

    merged += left[left_letter:]
    merged += right[right_letter:]

    return merged


def is_anagram(first_string: str, second_string: str):

    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    if first_string == '' or second_string == '':
        return (
            "".join(merge_sort_string(first_string_list)),
            "".join(merge_sort_string(second_string_list)),
            False,
        )

    first_string_sorted = "".join(merge_sort_string(first_string_list))
    second_string_sorted = "".join(merge_sort_string(second_string_list))

    return (
        first_string_sorted,
        second_string_sorted,
        first_string_sorted == second_string_sorted
    )
