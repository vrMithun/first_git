def t_c(G):
    V=len(G)
    Closure =[[0]*V for _ in range(V)]
    #To get value from G to CLOSURE
    for i in range(V):
        for j in range(V):
            Closure[i][j]=G[i][j]
    #Doing the Warshalls Alogorithm Main Formula
    for k in range(V):
        for i in range(V):
            for j in range(V):
                Closure[i][j]=Closure[i][j] or (Closure[i][k] and Closure[k][j])
    return Closure
G=[[0,0,0,0],[1,0,1,0],[1,0,0,1],[1,0,1,0]]
Ans=t_c(G)
print("Transitive Closure")
for row in Ans:
    print(row)