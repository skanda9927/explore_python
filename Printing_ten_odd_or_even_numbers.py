#
#To print first 10 odd or even numbers
#
print("enter the integer number from that number odd or even numbers to be printed\n");
number = int(input());
print ("\n press input number 1 for odd numbers to be printed \n input number 2 for even numbers to be printed")

choice = int(input());

if number % 2 == 0 : #checking odd or even numbers
    if choice == 1 :
        number = number+1 ; 
        for i in range(10) :
            print(number);
            number = number+2 ;
    else :  
        for i in range(10) :
            print(number+2);
            number = number+2 ;
         
        
else :        
    if choice == 1 :
         for i in range(10) :
            
            print(number+2);
            number = number+2 ;
        
    else :  
        number = number+1 ; 
        for i in range(10) :
            print(number);
            number = number+2 ;
        
        
           
    
    
       
    