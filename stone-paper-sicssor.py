
def game():
    set={'stone','paper','scissor'}
    l=list(set)
    i=''
    j=''
    a=str(input('enter your choise: '))
    print(l[0])
    if i==l[0]:
        print('you won!!!')
        i=str(input('do you want to play again: '))
        if i=="yes":
            return game()  
    else:
        print('you lost the game') 
        i=str(input('do you want to play again: '))
        if i=="yes":
            return game() 
print(game())           


