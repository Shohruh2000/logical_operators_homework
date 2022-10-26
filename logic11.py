def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==((a//10)*10 + a%10) and (a//10 < 100) and (a>99)

x = main(9990)
print(bool(x)) 
