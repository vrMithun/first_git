def check(s,l):
    if not s:
        return 0
    elif s[0]==l:
        return 1+check(s[1:],l)
    else:
        return check(s[1:],l)
print(check('aabbc','a'))
               
