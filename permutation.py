import random
import math
E =[]
U =[]
num = input('Enter any Number : ')
J = len(num)
for i in range(J):
    K =int(num[i])
    E.append(K)
print(E)

H = math.factorial(J)
print('The Number of Arrangement of this number is :',H)
p = 0
while p == 0:
    C = random.sample(E,len(E))
    print(C)
    if U.count(C) == 0:
        U.append(C)
    if len(U) == H:
        break

for d in range(H):
    Y = U[d]
    print(Y, end="")

        
        

    
    
    
