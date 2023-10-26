F=lambda:map(int,input().split())
n,k=F()
A=[1]+sorted(F())
print(A[k] if k==n or A[k+1]-A[k] else -1)
