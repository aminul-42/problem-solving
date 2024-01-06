#Write a program that reverses a given number.


n=int(input("Enter A Number [More than one character :]"))
number =n
reverse_number=0

while(n!=0):
    remainder= n % 10
    reverse_number=reverse_number * 10+ remainder
    n//=10  # // -> floor divison [ only return int number as result ]

    
print("Reverse of " ,number  ," : ",reverse_number)