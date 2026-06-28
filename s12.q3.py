def manage_marks():
   #taking 5 subject marks from user
   marks_list = []  #list to store marks of 5 subjects
   print("Enter marks for 5 sybjects: ")

   #taking 5 inputs using loop
   for i in range(1,6):
      while True:   #keep asking until valid input for each subject
         try:
            #get input and convert to float
            mark = float(input(f"Subject {i+1} marks:")) 

            if mark < 0 or mark > 100:
               print("Please enter marks between 0 and 70")
               continue

            marks_list.append(mark)
            break #exit while loop 
         
         except ValueError:
            #handles non_numeric input
            print("Error:Invalid input. Please enter a number only.")

    #calculate using list functions
      if len(marks_list) > 0:
         total = sum(marks_list)  
         average = total / len(marks_list)
         highest = max(marks_list)
         lowest = min(marks_list)

         #display results
         print("\n Mark Analysis")
         print("Marks entered: ",marks_list)
         print(f"Average marks: {average:.2f}")
         print("Highest marks:",highest)
         print("Lowest marks: ",lowest)

   #sort list in descending order
   marks_list.sort(reverse=True)   #reverse=True for descending
   print("Marks sorted (High to Low): ",marks_list)

#call the function
manage_marks()