def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a//10== a%10 and (9 < a and a < 99)

x = main(15)
print(bool(x))