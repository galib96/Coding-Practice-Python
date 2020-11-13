def reverse(x: int):
    """
    takes in integer and output it's reverse
    """
    result = 0
    if x < 0:
        x = x*(-1)
        a = -1
    else:
        a = 1
    while x > 0:
        carry = x%10
        result = result*10+carry
        x = x//10
    result = result*a
    if result < -2**31 or result > (2**31-1):
        return 0
    return result

print(reverse(12548963))