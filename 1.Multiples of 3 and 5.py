"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

n=int(input())
div_3=(n-1)//3
div_5=(n-1)//5
div_15=(n-1)//15

sum_3=div_3*(1+div_3)/2*3
sum_5=div_5*(div_5+1)/2*5
sum_15=div_15*(div_15+1)/2*15

print(sum_3+sum_5-sum_15)