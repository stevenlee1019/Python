''' Description
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
1
2
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string
'''
def between_markers(text: str, begin: str, end: str) -> str:
    
    
    s_idx = text.find(begin)
    if s_idx != -1:
        s_idx += len(begin)
    e_idx = text.find(end)

    if s_idx != -1:
        if e_idx != -1:
            if s_idx < e_idx:
                return text[s_idx:e_idx]
            else: 
                return ""
        else:
            return text[s_idx:] 
    else:
        if e_idx != -1:
            return text[:e_idx]
        else:
            return text

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
