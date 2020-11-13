def isPalindrome(x: int):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

print(isPalindrome(20011002))
    