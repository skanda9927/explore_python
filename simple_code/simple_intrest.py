#
## Find a simple interest for the given principal, rate_of_interest, time_duration
#
print ("\n enter the principle amount: \n ")
principal_amount = float(input ())
print ('enter the duration for which simple interest has to be calculated in years \n')
t = float(input())
print ('enter the rate  of interest per annum\n')
r = float( input())
simple_interest = (principal_amount * t * r) / 100
print ('\nSimple interest for principle {}, for {}years time, with {} as interest is: {}'.format(principal_amount, t, r, simple_interest))
