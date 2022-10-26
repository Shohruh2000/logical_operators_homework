def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a > 9 and a < 100) and ((a//10+a%10)%2==1)
answer = main(140)
print(answer)