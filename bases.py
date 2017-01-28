#!python

import string

def num_from_letter(letter):
    num = ord(letter) - 97 + 10
    return num

def letter_from_num(num):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return letters[num - 10]


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    # decimal number
    decimal_num = 0

    # Loop through and add
    for index, num in enumerate(str_num):
        num_to_add = int(num) if num.isdigit() else num_from_letter(num)
        decimal_num += num_to_add
        decimal_num *= base if index is not len(str_num) - 1 else 1

    # Return decimal num
    return decimal_num

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    # new base num
    new_base_num = ''

    # Loop through
    while num != 0:
        remainder = num % base
        num = num / base
        remainder = letter_from_num(remainder) if (remainder >= 10 and base > 10) else remainder
        new_base_num += str(remainder)

    # Reverse
    new_base_num = new_base_num[::-1]

    # Return
    return new_base_num

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36

    # Decode to base 10
    decimal_num = decode(str_num, base1)

    # Encode to new base
    new_base_num = encode(decimal_num, base2)

    # Return
    return new_base_num


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))

if __name__ == '__main__':
    main()
