def linear_search(list, target): 
    """
    Returns the index position of the target if found, else returns none 
    """

    for i in range(0, len(list)): 
        if list[i] == target:
            return i
    return None

def verify(index): 
    if index is not None: 
        print("The target is at index: ", index)
    else: 
        print("Target not found.")

numbers = range(0,10)

result = linear_search(numbers, 6)
verify(result)