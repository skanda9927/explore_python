#printing the prime numbers within the range of numbers
print("enter the 2 range of numbers to find prime numbers between the range \n please give range in ascending order\n")
print("enter the first number\n")
range1 = int(input())
print("enter the second number\n")
range2 = int(input())
n= range1 
i = range1
#n = int(input("Enter any number: "))
for i in range (range1,range2) :
    if i > 1:
        for x in range(2, i):
            if (i % x) == 0:
                #print(n, "is not a prime number")
                x=x+1 # break;
    else:
        print(n, "is a prime number")
       # i = i+1
else:
    print("prime numbers between",range1,"and",range2,"does not exist" )