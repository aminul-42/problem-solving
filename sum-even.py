#Write a program that finds the sum of all even numbers between 1 and `n`.


n=int(input("Enter The Range of Number From 1 to ..... :"))
i=1
sum=0


while(i<=n):
    if(i%2==0):
        print(i)
        sum+=i
    i+=1

print("The Sum of 1 to ",n ," = ",sum)
