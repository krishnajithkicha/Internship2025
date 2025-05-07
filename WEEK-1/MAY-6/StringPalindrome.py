#This program checks if a string is a palindrome or not.ie the entered string is same when reversed.
def string_palindrome(s):
    #s is the entered string
    s=s.lower() #converting the string to lower case 
    s=s.replace(" ","") #removing spaces from the string (No lemon)
    s=s.replace(",","") #removing commas from the string (No lemon,no melon)
    reversed_string=s[::-1] #reversing the string
    if s==reversed_string:
        return True #if the string is same when reversed, it is a palindrome
    else:
        return False #otherwise it is not a palindrome

string = input("Enter a string: ") #taking input from the user
if string_palindrome(string):
    print("The string is a palindrome.")
else:  
    print("The string is not a palindrome.")
