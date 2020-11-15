fibonacci=[1,2]
sum=0
i=0
#while len.fibonacci<=10:
while fibonacci[-1]<4000000: #will give us n+1+2 numbers because we already have two in
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
    i+=1
for j in range(1,len(fibonacci)): #will go through all positions and pick every third after the position of 2
    if j%3==1: # 1 4 7 10 13 ...
        sum+=fibonacci[j]
print(sum)