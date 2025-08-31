mssx=int(input("Enter x coordinate of your spaceship: "))
mssy=int(input("Enter y coordinate of your spaceship: "))
ess1x=int(input("Enter x coordinate of enemy spaceship1: "))
ess1y=int(input("Enter y coordinate of enemy spaceship1: "))
ess2x=int(input("Enter x coordinate of enemy spaceship2: "))
ess2y=int(input("Enter y coordinate of enemy spaceship2: "))
n=abs(mssx-ess1x)+(mssy-ess1y)
m=abs(mssx-ess2x)+abs(mssy-ess2y)
if n>m:
    print("attack the enemy spaceship2 at the coordinates",'(',ess2x,',',ess2y,')')
else:
     print("attack the enemy spaceship1 at the coordinates",'(',ess1x,',',ess1y,')')    

