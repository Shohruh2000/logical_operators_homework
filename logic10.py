def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==((a//10)*10 + a%10) and (a//10 < 10)

x = main(120)
print(bool(x)) 

