#Write a program that calculates the grade based on a given percentage.

number=float(input("Enter Your Mark Out Of 100 : "))

if(number>=80 and number <=100):
    {
        print("Your Number Is : ",number ," and Your Grade is A+ ")
    }
elif(number>=70 and number <=79 ):
    {
        print("Your Number Is : ",number ," and Your Grade is A ")
    }
elif(number>=60 and number <=69):
    {
        print("Your Number Is : ",number ," and Your Grade is A- ")
    }
elif(number>=50 and number <=59):
    {
        print("Your Number Is : ",number ," and Your Grade is B ")
    }
elif(number>=40 and number <=49):
    {
        print("Your Number Is : ",number ," and Your Grade is B- ")
    }
elif(number>=0 and number <=39):
    {
        print("Your Number Is : ",number ," and Your Grade is Fail ")
    }
else:
    {
        print("Your Input Mark is Invalid")
    }

