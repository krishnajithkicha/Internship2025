#This program converts celsius to fahrenhiet and fahrenhiet to celsius
def fahrenhiet_convertor(temp): #converts celsius to fahrenhiet
    F=(temp*(9/5))+32 #formula to convert celsius to fahrenhiet
    return F
def celsius_convertor(temp): #convert fahrenhiet to celsius
    C=(temp-32)*(5/9) #formula to convert fahrenhiet to celsius
    return C
choice=input("Enter 'c' to convert Fahrenhiet to Celsius and 'f' to convert Celsius to Fahrenhiet:") 
if choice=="c":
    temp=float(input("Enter the Fahrenhiet temperature to convert to Celsius:"))  
    c=celsius_convertor(temp) #converting fahrenhiet to celsius
    print("The Celsius Converted Temperature is:",c)
elif choice=="f":
     temp=float(input("Enter the Celsius temperature to convert to Fahrenhiet:"))
     f=fahrenhiet_convertor(temp) #converting celsius to fahrenhiet
     print("The Fahrenhiet Converted Temperature is:",f)
else:
    print("Please enter a valid choice")
