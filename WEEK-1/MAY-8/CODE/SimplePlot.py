import matplotlib.pyplot as plt

#Displaying Bar chart
student_names = ['Alan','Akhil','Kripa','Priya'] #List of student names
marks=[10,20,50,30] #List of marks obtained by the students
#Creating a bar chart using matplotlib
plt.bar(student_names,marks, color='green') #Creating a bar chart using matplotlib
#Adding title and labels to the chart
plt.title("Bar Chart")
plt.xlabel("Student-Names")    #X-axis label
plt.ylabel("Marks")          #Y-axis label
plt.savefig("studentmarks.png") #Saving the chart as a png file
#Displaying the chart
plt.show()
