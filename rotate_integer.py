#
# Rotate the string based on the given integer values for leftshift and rightshift, all test cases passed.

def left_rotate(S, pos):
    return S[pos:] + S[:pos]

def right_rotate(S, pos):
    return S[-pos:] + S[:-pos]