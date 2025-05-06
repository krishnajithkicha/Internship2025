#This program converts celsius to fahrenhiet and fahrenhiet to celsius
def fahrenhiet_convertor(temp): #converts celsius to fahrenhiet
    F=(temp*(9/5))+32
    return F
def celsius_convertor(temp): #convert fahrenhiet to celsius
    C=(temp-32)*(5/9)
    return C
choice=input("Enter 'c' to convert Fahrenhiet to Celsius and 'f' to convert Celsius to Fahrenhiet:")
if choice=="c":
    temp=float(input("Enter the Fahrenhiet temperature to convert to Celsius:"))
    c=celsius_convertor(temp)
    print("The Celsius Converted Temperature is:",c)
elif choice=="f":
     temp=float(input("Enter the Celsius temperature to convert to Fahrenhiet:"))
     f=fahrenhiet_convertor(temp)
     print("The Fahrenhiet Converted Temperature is:",f)
else:
    print("Please enter a valid choice")
