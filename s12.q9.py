import math

def unique():
    try:
        #taking sentence as input
        sentence = input("Enter a sentence: ").strip()
        
        #if it is empty
        if not sentence:
            print("Error: It is a empty sentence. Please enter some text.")
            return
        
        #extracting all unique words using set
        # split() breaks sentence into words
        # set() removes duplicates
        lst = sentence.split()
        unique_wrd = set(lst)
        
        #print the unique words in sorted order
        sorted_uq = sorted(unique_wrd)   
        print("\nUnique words {}".format(unique_wrd))
        print("Unique words in sorted order {}".format(sorted_uq))
        
        #now we are using math module to print total number of unique words raised to power 2
        total_uq= len(unique_wrd)
        sq_of_count = math.pow(total_uq, 2) 
        
        print("Total number of unique words {}".format(total_uq))
        print("Total unique words raised to power 2 {int}".format(sq_of_count))
        
    except AttributeError:
        print("Error: Invalid input type")
    except Exception as e:
        print("Something went wrong {}".format(e))

#calling function
unique()