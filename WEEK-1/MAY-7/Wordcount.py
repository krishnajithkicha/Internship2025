#This program is to count the word frequency
def word_frequency(f):   #Function counts the number of words in the provided text file
    data=f.read()       #reads the entire file
    word=data.split()   #splits the entire file into words
    word_count=0
    print("The contents in the text file are:",end="\n")
    for i in word:
        word_count+=1   #counts the number of words in the file
        print(i,end=" ")
    return word_count
try :   #checks whether the file exits or not
    f = open('C:\\Users\\User\\Desktop\\INTERNSHIP\\Internship2025\\WEEK-1\\MAY-7\\Apple.txt', 'r')
    count=word_frequency(f)
    if count!=0: #prints if the file is not empty
        print("\nThe Word frequency of the text file is:",count)
    else:
        print("The file is empty")
except FileNotFoundError: #raises error when file is not found
    print("No file exists")