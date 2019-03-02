num = int(input('Put a number here'))
if num > 1:
        
    for i in range (2,num):
        if num % i == 0:
            print ("This isn't a prime number")
            break
    else:
         print ("This is a prime number")
#End of the program