#Write a program that finds the maximum of three numbers.

a=float(input("Enter 1st Number: "))
b=float(input("Enter 2nd Number: "))
c=float(input("Enter 3rd Number: "))


if(a>b and a>c):
    {
        print("A is Maximum Number = ",a)
    }
elif(b>a and b>c):
    {
        print("B is Maximum Number = ",b)
    }
else:
    {
        print("C is Maximum Number = ",c)
    }

