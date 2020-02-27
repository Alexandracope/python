ISBN=input('Please input your ISBN 12 digit code:')
sum1=0
sum2=0
for index in range (0,12,2):
    temp=int(ISBN[index])
    sum1=sum1+temp
for index2 in range(1,12,2):
    temp2=int(ISBN[index2])*3
    sum2=sum2+temp2
total=sum1+sum2
remainder=total%10
X13=10-remainder
print(ISBN +str(X13))
