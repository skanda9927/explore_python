#
## a program to find the compound interest
# 
# 
print ('Enter the principle amount: ')
p = float(input ())
print ('enter the duration for which compound interest has to be calculated in years \n')
t = float(input())
print ('enter the rate  of interest per annum\n')
r = float ( input())
i = p * ((1 + r) / 100) * t
## TIP: to print message/text formatted manner, use %() notation
print ('\n compound  interest as per given data is : %10.2f' % (i))

## PEP8 - Python coding standard 