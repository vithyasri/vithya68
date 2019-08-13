O=int(input())
M=[]
for j in range(O):
	T=input()
	M.append(T)
U=min(M)
C=len(U)
for j in range(1,C+1):
 
	B=T[0:j]
	if all(B==i[0:j] for i in M):
		Z=B
print(Z)
