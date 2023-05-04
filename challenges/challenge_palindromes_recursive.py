def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    if len(word) == 1 or low_index >= high_index:
        return True

    if len(word) == 2 and word[low_index] == word[high_index]:
        return True

    if len(word) >= 3 and word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False
