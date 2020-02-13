'''
Function to check whether an integer is a palindrome or not.
'''
def is_palindrome(int_to_check):

    # Convert integer to string representation because of easier manipulation/reading
    string_representation = str(int_to_check)

    # Create two arrays, one to store characters of string in original order and one in reverse order for comparison purposes
    array_for_integers_in_order = []
    array_for_integers_in_reverse_order = []

    # Add characters in original order to array
    for x in string_representation:
        array_for_integers_in_order.append(x)

    # Uncomment line below to check what is actually contained in the ordered array. (For internal testing)
    # print(array_for_integers_in_order)

    # Traverse from tail of string and add to reverse ordered array. (Split into two lines for readability)
    for x in string_representation:
        character_to_add = (string_representation[len(string_representation) - string_representation.index(x) - 1])
        array_for_integers_in_reverse_order.append(character_to_add)

    # Uncomment line below to check what is actually contained in the ordered array. (For internal testing)
    # print(array_for_integers_in_reverse_order)

    if(array_for_integers_in_order == array_for_integers_in_reverse_order):
        return True

    return False



'''
Test Cases
'''
print(is_palindrome(1))
print(is_palindrome(12))
print(is_palindrome(121))
print(is_palindrome(135797531))
print(is_palindrome(5165148))
print(is_palindrome(-5))
