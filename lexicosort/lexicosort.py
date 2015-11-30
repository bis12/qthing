#!/usr/bin/env python
import string
import sys

def arbitrary_sort(given, order):
    '''This function will take a list of strings and return them
    in sorted order where order is a string of characters
    in an arbitary order.

    This will only work on lowercase ascii characters!'''
    if sys.version_info < (3,):
        strmod = string
    else:
        strmod = str
    trans = strmod.maketrans(order, string.ascii_lowercase[:len(order)])

    def score(word):
        return word.translate(trans)

    return sorted(given, key=score)


def help():
    help = '''
    Provide a list of strings to be sorted for arguments 1..n-1 and
    a lexicographic sort order as argument n. Empty strings can be
    provided as a pair of quotes but will only be present in the
    returned string as a length 0 string that is seperated from other
    output by spaces.

    Returns the arguments sorted into the order given.

    Examples:
    $ {pname} acb abc bca abc
    abc acb bca
    $ {pname} acb abc bca cba
    bca acb abc
    $ {pname} aaa aa "" a
     aa aaa
    '''.format(pname=sys.argv[0])
    print(help)
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3 or '-h' in sys.argv or '--help' in sys.argv:
        help()
    print(' '.join(arbitrary_sort(sys.argv[1:-1], sys.argv[-1])))
