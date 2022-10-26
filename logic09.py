def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1 = (a%2==1 and b%2==1)
    x2 = (a%2==0 and b%2==1)
    x3 = (a%2==1 and b%2==0)
    return x1 or x2 or x3

answer = main(5,7)
print(answer)