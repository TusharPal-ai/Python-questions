a=int(input("enter ur number"))

for i in range(2,a):
    if(a%i)==0:
        print("the number is not prime ")
        break
else:
    print("the numer is pirme")