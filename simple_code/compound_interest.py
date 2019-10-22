#compund interest
print ("\n enter the principle amt \n ")
p = int(input ())
print ('enter the duration for which compound interest has to be calculated in years \n')
t = int (input())
print ('enter the rate  of interest per annum\n')
r = int ( input())
i = p*((1+r)/100)*t
print ('\n compound  interest as per given data is ',i)