import re


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
    x1=a%10


    return (x5==(x4+1) and x4==(x3+1) and x3== (1+x2)and x2==(x1+1)) and (10000<=a and a<=99999)
    return x1,x2,x3,x4,x5

answer = main(543219)
print(answer)
