#Floyd's Algorithm
Inf =999
def print_sol(d):
    for i in range(len(G)):
        for j in range(len(G[i])):
            if (d[i][j] ==Inf):
                print("Inf",end=" ")
            else:
                print(d[i][j],end=" ")
        print()        
def  Floy(G):
    d=list(map(lambda i: list(map(lambda j:j,i)),G))
    print(d)
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                    d[i][j]=min(d[i][j],d[i][k]+d[k] [j])
    print_sol(d)

G=[[0,409,389,429,119],[409,0,109,239,379],[389,109,0,229,319],[429,239,229,0,309],[119,379,319,309,0]]
Floy(G)