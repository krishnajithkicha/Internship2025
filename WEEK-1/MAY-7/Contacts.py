#This program add contacts using dictionary and get the details from the text file
def addcontacts(): #Function add the contact details into the dictionary
    contactbook=dict() #creating dictionary called contactbook
    num=int(input("Enter the number of contacts:")) #Asks user to enter the number of contacts to be added
    print("Enter the details of the contacts:")
    for i in range(num): 
        sno=int(input("Enter the serial number:"))
        name=input("Enter the name of the contact:")
        phno=int(input("Enter the phone number:"))
        contactbook[sno]={"Name":name,"Phone":phno}     #adding the details into the dictionary
    return contactbook
def savecontact(contactbook): #Function to save the contact details into the text file
    f=open("Contact.txt",'a') #opens the file in append mode so that the exiting data is not overwritten
    for key,value in contactbook.items(): 
        f.write(f"Serial Number: {key}, Name: {value['Name']}, Phone: {value['Phone']}\n") #writes the details into the file
    f.close()
    print("The contacts are saved into the file successfully")
    try:
        f=open("Contact.txt",'r')
        print("The Contacts  in the text file are: \n")
        print(f.read()) #reads the file and prints the contents of the file
    except FileNotFoundError:
        print("The file not found")
details=addcontacts() #calls the function to add the contacts
savecontact(details) #calls the function to save the contacts

