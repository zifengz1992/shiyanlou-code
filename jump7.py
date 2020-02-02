a=0
while a>=0 and a<=99:
    a=a+1
    if a%7==0:
        continue
    elif a%10==7:
        continue
    elif a>=70 and a<=79: ##a//10==7
        continue
    print(a)
