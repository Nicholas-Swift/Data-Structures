#!python

import string

def num_from_letter(letter):
    num = ord(letter) - 97 + 10
    return num

def letter_from_num(num):
    letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    return letter_array[num - 10]

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    # decimal number
    decimal_num = 0

    # Reverse string
    str_num = str_num[::-1]

    # For loop through string adding to decimal num
    for index, num in enumerate(str_num):

        # number to add
        num_to_add = 0

        # Check if letter
        if num.isdigit():
            num_to_add = int(num)
        else:
            num_to_add = num_from_letter(num)

        # Add to decimal num
        decimal_num += num_to_add * (base ** index)

    # Return decimal num
    return decimal_num

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    # new base number
    new_base_num = ''

    # Loop through and add remainders to new_base_num
    index = 0
    while num != 0:
        remainder = num % base
        num = num / base

        # Turn remainder into letter if needed
        if remainder >= 10 and base > 10:
            remainder = letter_from_num(remainder)

        new_base_num = new_base_num + str(remainder)
        index += 1

    # Reverse string
    new_base_num = new_base_num[::-1]

    # Return new base
    return new_base_num

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number

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

def nick_test():
    print(decode('cat', 32))

if __name__ == '__main__':
    nick_test()
