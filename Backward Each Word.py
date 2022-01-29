''' Description 
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

Example:

backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'
'''
def backward_string_by_word(text: str) -> str:
    # your code here

    arr = text.split(" ")

    for x in range(len(arr)):
        arr[x] = arr[x][::-1]

    return " ".join(arr)



if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
