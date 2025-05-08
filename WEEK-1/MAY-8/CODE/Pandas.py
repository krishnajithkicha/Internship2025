#This program is to understand about pandas
import pandas as pd


#Reading the data from csv file
df=pd.read_csv("students.csv")
print("The datas in the csv file are:")
print(df) #printing the data in the csv file as dataframe

#for printing specific column 
print("***Displaying the Name,Age,Gender and Department of the students***")
print(df[['Name','Age','Gender','Dept']]) #Printing the specific columns of the dataframe


print("Displaying the first 5 rows:",df.head()) #Prints First 5 rows
print("Displaying the last 5 rows:",df.tail()) #Prints Last 5 rows
print("Displays the shape:",df.shape) #prints (rows,columns)
print("Displays the columns :",df.columns) #prints column names
print("Displays the nonnull columns:",df.info()) #prints data types and nulls
print("The summary statistics of the marks obtained by the students:",df['Marks'].describe()) #summary statistics

#FILTERING 
print("The passed students are: \n",df[df['Passed']=='Yes']) #Filtering the students who passed
print("The students in department computer science with marks above 90: \n",df[(df["Dept"] == "Computer Science") & (df["Marks"] > 90)]) #Filtering the students in department computer science with marks above 90

#SORTING
print("The sorted students:\n",df.sort_values(by=["Yr", "Attend"], ascending=[True, False])) #Sorting the students by year and attendance in ascending order

#GROUPING AND AGGREGATION
print("The Mean marks of the students in corresponding department:\n",df.groupby("Dept")["Marks"].mean()) #Grouping the students by department and calculating the mean marks of the students in corresponding department
print("The marks of student by department:\n",df.groupby('Dept')['Marks'].sum()) #sum of marks