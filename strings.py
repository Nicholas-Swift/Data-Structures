#!python

import string


def is_substring(text, substring):
    """Iteratively check whether a given string is a substring iteratively"""
    new_substring = ""
    for i in text:
        new_substring += i

        if new_substring == substring:
            return True

        if len(new_substring) >= len(substring):
            new_substring = new_substring[1:]

    return False


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """Best case: Omega(n/2)"""
    """Worst case: O(n)"""

    # First setting indexes
    first_index = 0
    last_index = len(text) - 1

    while(first_index <= last_index):

        # Get letters only
        while not text[first_index].isalpha():
            first_index += 1
            if first_index > len(text) - 1:
                return True
        while not text[last_index].isalpha():
            last_index -= 1
            if last_index < 0:
                return True

        # Not same, return
        if(text[first_index].lower() != text[last_index].lower()):
            return False

        first_index += 1
        last_index -= 1

    return True


def is_palindrome_recursive(text, first_index=None, last_index=None):

    # For first
    if first_index is None or last_index is None:
        first_index = 0
        last_index = len(text) - 1

    # End
    if first_index >= last_index:
        return True

    # Check letters
    if not text[first_index].isalpha():
        return is_palindrome_recursive(text, first_index + 1, last_index)
    if not text[last_index].isalpha():
        return is_palindrome_recursive(text, first_index, last_index - 1)

    # Not same, return
    if(text[first_index].lower() != text[last_index].lower()):
        return False

    return is_palindrome_recursive(text, first_index + 1, last_index - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
