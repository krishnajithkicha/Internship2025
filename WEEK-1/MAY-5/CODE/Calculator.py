def calculator(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        if num1>num2:
            return num1-num2
        else:
            return num2-num1
    elif operator=="*":
        return num1*num2
    elif operator =="/":
        if num2!=0:
            return num1/num2
        else:
            print("Math Error: Division by zero")
            return None
    else:
        print("Math Error: Invalid operator")
        return None
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator (+, -, *, /): ")
result=calculator(num1,num2,operator)
if result is not None:
    print("The result of ",num1," ", operator," " ,num2," = ",result)