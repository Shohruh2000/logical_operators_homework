def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return  (a%2==1 and b%2==1) or (a%2==0 and b%2==1) or (a > 0 and b > 0)

x = main(4,6)
print(bool(x))