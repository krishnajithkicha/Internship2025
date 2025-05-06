#This program is for understanding the purpose of exception handling in Loginpage
def registration():   #user registration 
    user_details=[]
    username=input("Enter your username:") #taking username as input from the user
    password=input("Enter your password:") #taking password as input from the user
    user_details.append(username) #appending username to the list
    user_details.append(password)   #appending password to the list
    return user_details

def login(username,password): #user login
    entusername=input("Enter your username:")   #taking username as input from the user
    entpassword=input("Enter your password:") #taking password as input from the user
    try:                                            
        if entusername==username and entpassword==password: #checking if the entered username and password are same as the registered username and password
            #if they are same, the user is logged in successfully
            print("The user login is sucessfull")
        else:
            raise ValueError("Invalid username or password")    #if they are not same, a ValueError is raised with the message
    except ValueError as e: #catching the ValueError
        print(e)

print("***Welcome to registration page***")     
usedetails=[]
usedetails=registration() #calling the registration function to register the user
print("User registered successfully")
username=usedetails[0]
password=usedetails[1]
print("****Welcome to Login page****")
login(username,password)    #calling the login function to login the user