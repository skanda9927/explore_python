#
## Checking for type of triangle based on Length of sides.
#
###  PSeudocode ###
#   1. Read the Length, Base and Hypotenuse of triangle
#   2. 
#
#
###
print("Enter the length of hypotenuse of triangle: ") ;
hypotenuse = int(input());

base = int(input("The length of the base of triangle: "));

print("the length of height of triangle");
height = int(input());

print("The Hypotenuse, Base and Height of the triangle are: {}, {}, {}".format( hypotenuse, base, height))
print("The Hypotenuse, Base and Height of the triangle are: %s, %s, %s" % (hypotenuse, base, height))
if height == base :
    print("its a isoceles triangle") ;

elif hypotenuse*hypotenuse == ((base*base) +(height*height)) :
    print("its a right angle triangle") ;
    
else :
     print("its scalene triangle")
