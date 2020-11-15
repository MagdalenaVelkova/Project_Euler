"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
n=int(input())
primes=[2]
for i in range(2,n+1):
    div=0
    for j in range (len(primes)):
        if i%primes[j]==0:
            div+=1
    if div==0:
        primes.append(i)