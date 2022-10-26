def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a > 9999 and a < 1000000) and ( a%2 ==0 or a%2 == 1 )

answer = main(12356)
print(answer)
