def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer 54321
    """
    x1 = a%10
    x2 = (a//10)%10
    x3 = (a//100)%10
    x4 = ((a//100)//10)%10
    x5 = a//10000

    return (x5==(x4+1) and x4==(x3+1) and x3== (1+x2)and x2==(x1+1)) and (9999<a and a<100000)

answer = main(87654)
print(answer)
