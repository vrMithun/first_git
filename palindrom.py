
def palindrome(i,len):
    s='madam'
    if s[0]==s[len-1]:
        if i!=len:
            return palindrome(i+1,len-1)
        else:
            print('it is palindrome')
    else:
        print('it is not palindrome')
print(palindrome(0,5))