N=int(input())
 
A=[0]*N
 
for x in range(N):
    i=int(input())
    r=int(input())
    c=int(input())
    A[x]=[i,r,c]
 
M=int(input())
 
for x in range(M):
    i=int(input())
    for item in range(N-1,-1,-1):
        if A[item][0]<=i<=A[item][1]:
            print(A[item][2], end=' ')
            break
    else:
        print(0)