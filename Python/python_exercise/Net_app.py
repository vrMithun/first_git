def myfunc(n,a,m,plan_list):
    result=0
    i=1
    while i<=n:
        min_amount=107
        min_index=0
        for j in range(m):
            if i>=plan_list[j][0] and i<=plan_list[j][1]:
                if plan_list[j][2]<a:
                    if min_amount>plan_list[j][2]*plan_list[j][3]:
                        min_amount=plan_list[j][2]*plan_list[j][3]
                        min_index=j
                else:
                    if min_amount>plan_list[j][3]*a:
                        min_amount=plan_list[j][3]*a
                        min_index=j
        result=result+min_amount*(plan_list[min_index][1]-i+1)
        i=plan_list[min_index][1]+1
    return result

n,a,m=map(int,input().split())
plan_list=[]
for i in range(m):
    plan_list.append(list(map(int,input().split())))
print(myfunc(n,a,m,plan_list))
        
            