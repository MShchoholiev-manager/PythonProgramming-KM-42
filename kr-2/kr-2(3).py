def palindrome(string):
    
    s = ''.join(string.split()).lower()

    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindrome(s[1:-1])

print(palindrome('A butt tuba'))
