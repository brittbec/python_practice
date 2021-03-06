def merge_sort(list):
    """
    Sorts list in ascending order
    Returns a new sorted list

    Divide: Finds the midpoint of list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step

    Overall O(kn log n) runtime
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    # recursive portion of the function
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    divide the unsorted list at midpoint into two sublists
    Return two sublists -- left and right
    Takes overall O(log n) runtime
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l


aList = [1, 5, 3, 6, 32, 56, 2, 4]

print(aList)
l = merge_sort(aList)


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


print(verify_sorted(aList))  # Should return false
print(verify_sorted(l))  # Should return true
