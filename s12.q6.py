import random
import math  

def setAndtuple():
    s = set()  
    print("Enter 10 numbers:")
    
    # Taking 10 numbers
    for i in range(10):
        while True:
            try:
                num = float(input("Enter number {} ".format({i+1})))
                s.add(num)  
                break
            except ValueError:
                print("Error: Please enter a valid number only.")
    
    #now we will convert set to tuple
    n = tuple(s)
    print("Unique number stored in set {}".format(s))
    print("Converted to tuple {}".format(n))
    
    #now we will use random module to pick 3 random numbers
    try:
        if len(n) < 3:
            print("\nLess than 3 unique numbers. Can't pick 3 random numbers.")
        else:
            rand_pick = random.sample(n, 3)
            print("3 random numbers from tuple {}".format(rand_pick))
    except Exception as e:
        print("Error while picking random numbers {}.format(e)")
    
    #now we will using math module
    try:
        t = sum(n)
        if t < 0:
            print(f"Sum of tuple = {t}. Can't find square root of negative number.")
        else:
            sq_sum = math.sqrt(t)
            print("Sum of all tuple elements {}".format(t))
            print("Square root of sum {:.2f}".format(sq_sum))
    except Exception as e:
        print("Error while calculating square root {}".format(e))


# Call the function
setAndtuple()