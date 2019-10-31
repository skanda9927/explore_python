#
## 1. Find if a given number is odd or even
#
#import time
#time.sleep(5)

import sys
import os

if (len(sys.argv)) == 2:
	n = int(sys.argv[1])
elif (os.environ.get('NUMBER')):
	n = int( os.environ.get('NUMBER'))
else:
	print ("\nEnter the number: ")
	n = int(input ())

if n % 2 == 0:
    print('\n',n,'the number inputed is even')
else:
    print('\n number inputed',n,' is odd')
    
