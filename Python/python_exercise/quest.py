import random    #importing random function
import string   #importing string function
from linkedList import * #import the linked list file that is linkedList.py
class player:#creating a class named player
    def __init__(self,ID):#creating id for new player
        self.ID=ID  #defining players id
        self.lst=LinkedList()  #creating an object named LinkedList() it also automatically creates head element.
        self.player_quest()   #calling the player_quest() method.
        self.quest=self.lst.traversal()    #printing the quest details of the player
    def player_quest(self):
        n=random.randint(1,10)  #randomly generating a number from 1 to 10.
        alphabets = string.ascii_letters #generating the string 'abcdefgh....ABCDEFGH...' 
        for i in range(n):
            self.lst.add(random.choice(alphabets),i)   #randomly select a letter from the alphabets string
player1=player(1)                                      #random.cohice used because it returns a value from a given data.
player2=player(2)    #creating two players object.
player3=player(3)
'''here linked list got imported from the file that i have created 'linkedList.py'.
the reason that i have used linked list is the quest generated here are random and 
we dont know the number of quest for each players. so linked list will come in handy here.
we no need to specify any fixed length for the linked list and can be store the values until your computer
memory gets over.'''

#time complexity is O(1)
             
        
