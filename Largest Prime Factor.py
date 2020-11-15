n=int(input())
primes=[2]
for i in range(2,n+1):
    div=0
    for j in range (len(primes)):
        if i%primes[j]==0:
            div+=1
    if div==0:
        primes.append(i)