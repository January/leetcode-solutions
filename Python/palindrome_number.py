def isPalindrome(x: int) -> bool:
    str_num = str(x)
    return str_num is str_num[::-1]