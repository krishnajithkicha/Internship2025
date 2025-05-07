#This program asks user input and saves into a file and reads the saved input
def writetofile(): #function to write to the file
    f=open("sample.txt",'w') #opens the file in write mode so that the existing data is overwritten
    num=int(input("Enter the number of lines of sentences to be added:")) 
    print("Enter the text for the file line by line:")
    for i in range(num):
        data=input()
        f.write(data) #writes the data to the file
        f.write("\n")
    f.close()
    print("The contents in the text file are: \n")
    f=open("sample.txt",'r') #opens the file in read mode to read the contents of the file
    data=f.readlines() #reads the file line by line and stores it in the list called data
    for i in data:
        print(i)
writetofile() #calls the function to write to the file and read the contents of the file