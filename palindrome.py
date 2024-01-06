# Write a program that checks if a given string is a palindrome.

#A string is said to be a palindrome 
# if the reverse of the string is the same as the string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

'''
What have we done here?  

In the above code, we start by declaring the isPalindrome() function and passing the string argument.  
Then, we define two variables first and last and assign them with values 0 and len(string) -1 respectively. In the above code, we enter an input string. 
Next, we use the while loop to iterate all characters of the input string from start to end. The loop will evaluate whether or not the nth index value from the front matches the nth index value from the back. If True, the function returns that the string is a palindrome.  
If the first and last characters don’t match, then the loop breaks right away and does not check the entire string (unlike the for loop). 

'''



def is_palindrome(string):
    string=string.lower().replace('',"")
    first=0 
    last=len(string)-1

    while(first<last): 
        if(string[first]==string[last]): 
            first=first+1 
            last=last-1 
        else:
            return "The String Is Not Palindome"
    return "The String is a palindrome"

str1=input("Enter String  : ")
print(is_palindrome(str1))