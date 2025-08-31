king=[]
bishop=[]
rook=[]
i=0
j=0
k=0
for i in range (0,2):
    king.append(int(input()))    
for j in range (0,2):
    bishop.append(int(input()))
for k in range (0,2):
    rook.append(int(input()))   
if (king[0]==rook[0] and king[1]!=rook[1]) or (king[0]!=rook[0] and king[1]==rook[1]):
    print('check given by rook')
if abs(king[0]-bishop[0])==1 and abs(king[1]-bishop[1])==1:
    print('check given by bishop')