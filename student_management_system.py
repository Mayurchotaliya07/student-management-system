import mysql.connector

class students:
    def __init__(self,host,user,password,database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor()
        print("Database connected succesfull")

    def add(self,name,age,grade):
        query = "INSERT INTO student_info (name, age, grade) VALUES (%s, %s, %s)"
        self.cursor.execute(query,(name, age, grade))
        self.conn.commit()
        print("Student added succesfully")

    def view_student(self):
        query = "SELECT * FROM student_info"
        self.cursor.execute(query)
        student = 0
        for row in self.cursor.fetchall():
            student += 1
            print(row)
        print(f"{student} students displayed")

    def update(self,name,age,grade,id):
        query = "UPDATE student_info SET name=%s, age=%s, grade=%s WHERE id=%s"
        self.cursor.execute(query ,(name, age, grade, id))
        self.conn.commit()
        print("Update succesfully")

    def delete(self,id):
        query = "DELETE FROM student_info WHERE id=%s"
        self.cursor.execute(query ,(id,))
        self.conn.commit()
        print("Delete succesfull")

    def close(self):
        self.cursor.close()
        self.conn.close()

    def menu(self):
        
        print("Welcome to the student management system What you wanted to do \n1) Add new student \n2) View student list \n3) Update student \n4) Delete student \n5) Exit")

        while True:
            try:
                user_input = int(input('Enter a number from 1 to 5 only: '))
            except ValueError:
                print("Enter correct value")
                continue

            if user_input == 1:
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                grade = input("Enter grade: ")
                self.add(name,age,grade)
                
                
            elif user_input == 2:
                self.view_student()
                
            
            elif user_input == 3:
                id = int(input("Enter id to update: "))
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                grade = input("Enter new grade: ")
                self.update(name, age, grade, id)

                

            elif user_input == 4:
                id = int(input("Enter id number that you want to delete: "))
                self.delete(id)
                

            elif user_input == 5:
                break

            else:
                print("Enter correct number")

            ask_user = input("Do you want to see main menu or you want to quit(yes or no only): ").lower()
            try: 
                if ask_user == "yes":
                    continue
                elif ask_user == "no":
                    print("Bye")
                    break
            except ValueError:
                print("Enter correct value")


db = students("localhost","root","Your password","students")

db.menu()
db.close()