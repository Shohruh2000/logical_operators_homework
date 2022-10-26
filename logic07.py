def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1 = (a<0 and b<0)
    x2 = (a>0 and b<0)
    x3 = (a<0 and b>0)
    return x1 or x2 or x3

answer = main(8,6)
print(answer)