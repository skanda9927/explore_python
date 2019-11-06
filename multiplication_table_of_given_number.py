#
## Printing multiplication table
#

print("enter the number whose multiplication table has to be genrated: ")
number = int( input())
print("enter the multiplier till which multiplication table has to end: ")
multiplier = int( input())

# Loop over count 'multiplier' times
count = 1
while count <= multiplier:
    # Print the multiplication table - 1 row at a time.
    print("%2d * %2d = %3d" % (number, count, number * count))
    count = count + 1

for i in range(1,multiplier+1) : 
    print(number,"*",i,"=",i*number) ;


## Handle reading number, multiplier as below
    # a. Command line while executing
    # b. Environment variables (  NUMBER and MULTIPLIER)
    # c. inputs.txt File which has 2 numbers in in 2 lines.


