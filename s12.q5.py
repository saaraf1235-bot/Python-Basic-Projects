def student_database():
    students = {}  
    
    while True:
        print("\n---Displaying Student Database Menu---")
        print("1. Add student")
        print("2. Search student by roll number")
        print("3. Display all students")
        print("4. Exit")
        
        try:
            choose= int(input("Enter your choice (1-4): "))
            
            if choose == 1:
                try:
                    roll_no = int(input("Enter roll number: "))
                    
                    #checking if roll no is already exist
                    if students.get(roll_no):
                        print("Error: Roll number {} already exists.".format(roll_no))
                        continue
                    
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    city = input("Enter city: ")
                    
                    
                    students.update({roll_no: {'name': name, 'age': age, 'city': city}})
                    print("Student {} added successfully.".format(name))
                    
                except ValueError:
                    print("Error: Roll number and age must be numbers only.")
            
            elif choose == 2:
            
                try:
                    searching_roll = int(input("Enter roll number to search: "))
                    
                    #using get() for safely accessing dictionary
                    s_info = students.get(searching_roll)
                    
                    if s_info:
                        print("Roll No {}".format(searching_roll))
                        print("Name {}".format(s_info['name']))
                        print("Age {}".format(s_info['age']))
                        print("City {}".format(s_info['city']))
                    else:
                        print("No student found with roll number {}".format(searching_roll))
                        
                except ValueError:
                    print("Error: Please enter a valid roll number.")
            
            elif choose == 3:
                if not students:
                    print("Database is empty.No records. No students to display.")
                else:
                    print("\n--- Student Records ---")
                    print("Roll No | Name | Age | City")
                    print("---------------------------------")
                    for roll, details in students.items():
                        print(f"{roll} | {details['name']} | {details['age']} | {details['city']}")
            
            elif choose == 4:
                print("Exiting. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please select between 1-4.")
                
        except ValueError:
            print("Error: Please enter a valid number .")


#calling function
student_database()