def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return (a%2==1 and b%2==1) and (a>0 and b>0 ) or (a==b)

x = main(12,11)
print(bool(x))