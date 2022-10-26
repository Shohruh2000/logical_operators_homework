def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return (a<0 and (b) <0 ) and (a % 2 ==0 or a % 2 ==1 ) and (b % 2 ==0 or b % 2 ==1) 

x = main(-2 , -7)
print(bool(x))