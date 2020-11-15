n=int(input())
div_3=(n-1)//3
div_5=(n-1)//5
div_15=(n-1)//15

sum_3=div_3*(1+div_3)/2*3
sum_5=div_5*(div_5+1)/2*5
sum_15=div_15*(div_15+1)/2*15

print(sum_3+sum_5-sum_15)