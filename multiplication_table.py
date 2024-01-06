#Write a program that prints the multiplication table of a given number.


n = int(input("Enter A Numebr  = "))
print( " Multiplication Table For " , n  , " :")

for i in range(1,11):
    print(n , "*" ,  i , " = " ,n*i)

