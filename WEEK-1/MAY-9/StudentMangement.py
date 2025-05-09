#Student Management Platform where we can add,delete,search students

class StudentManagement:
    def __init__(self):
        self.students=[]
    
    def addstudent(self,student_id,stname,age):
        for i in self.students:
            if i["id"]==student_id:
                print("The student already exists")
        self.students.append({"id":student_id,"name":stname,"age":age})
        print("The student successfully added")
  
    def removestudent(self,student_id):
        for i in self.students:
            if i["id"]==student_id:
                self.students.remove(i)
                print("The Student removed successfully")
                return
            
        print("No such student exists")
    
    def searchstudent(self,student_id):
        for i in self.students:
            if i["id"]==student_id:
                print("The student with id :",i["id"],"name:",i["name"],"age:",i["age"])
                return
        print("No student found")

    def displaystudent(self):
       if not self.students:
           print("No students to display")
       else:   
           for i in self.students:
               print("ID:",i["id"],"Name:",i["name"],"Age:",i["age"])

def main():
    print("******WELCOME TO ABM SCHOOLS******")
    st=StudentManagement()
    choice=input("Enter 'c' to continue the school operations or 'q' to exit from the application :")

    while True:
        if choice=='q':
            print("Exiting from the application.\n Thank You")
            break
        elif choice=='c':
            print("The operations in the School are: \n")
            print("1.Add students \n")
            print("2.Delete students \n")
            print("3.Search students \n")
            print("4.Display students")
            ch=int(input("Enter your choice from 1-4 for performing the operations:"))
            if ch==1:
                print("ADDING STUDENTS \n")
                numb=int(input("Enter the number of students to add:"))
                for i in range(numb):
                    sid=int(input("Enter the student id:"))
                    sname=input("Enter the student name:")
                    sage=int(input("Enter the age of student:"))
                    st.addstudent(sid,sname,sage)
                choice=input("Please Enter 'c' to continue the school operations or 'q' to exit from the application :")
            elif ch==2:
                print("DELETE STUDENTS \n")
                n=int(input("Enter the number of students to delete:"))
                for i in range(n):
                    sid=int(input("Enter the student id to delete:"))
                    st.removestudent(sid)
                choice=input("Please Enter 'c' to continue the school operations or 'q' to exit from the application :")
            elif ch==3:
                print("SEARCHING STUDENTS")
                n=int(input("Enter the number of students to search:"))
                for i in range(n):
                    sid=int(input("Enter the student id to search:"))
                    st.searchstudent(sid)
                choice=input("Please Enter 'c' to continue the school operations or 'q' to exit from the application :")
            elif ch==4:
                print("DISPLAYING THE STUDENTS")
                st.displaystudent()
                choice=input("Please Enter 'c' to continue the school operations or 'q' to exit from the application :")
            else:
                print("Please enter a valid choice")
if __name__=="__main__":
    main()