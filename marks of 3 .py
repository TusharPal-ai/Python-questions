mark1=int(input("enter ur marks for first subject"))
mark2=int(input("enter ur marks for second subject"))
mark3=int(input("neter marks for third subject"))
a= mark1 + mark2 + mark3
print("sum of all marks=" ,a)
per=a*100/300
print("percentage of the makrs out of 300 is ",per )
if(per<=30):
    print("u ahev failed teh exams")
else:
    print("u have passed the exams")
    