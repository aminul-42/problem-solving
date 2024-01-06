# Write a program that calculates the factorial of a number.

# n! = n * ( n - 1 ) * ( n - 2 ) * ....* 1 


num = int(input("Enter a number: "))

factorial = 1


if (num < 0 ):
   print("Sorry ! factorial does not exist for negative numbers")
elif (num == 0):
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
         factorial = factorial*i
print("The factorial of",num,"is",factorial)
         

          
      
         
       
   



