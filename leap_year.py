#Write a program that determines if a year is a leap year or not.

#If year % 4 = 0 AND year % 100!= 0 OR year%400 == 0

year=int(input("Enter A Random Year: "))

if(year%4==0 and year % 100!=0 or year%400==0):
    {
        print(year," Is a Leap Year")
    }
else:
    {
        print(year," Isn't a Leap Year")
    }
