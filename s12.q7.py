def square():
    try:
        # Lambda function to calculate square
        sq= lambda x: x * x
        
        #using range(1, 21) to generate numbers 1 to 20
        num = range(1, 21)
        
        #stores the squares of these numbers in a list using the lambda function
        sq_list = [sq(num) for num in num]
        print("All squares from 1-20: {}".format(sq_list))
        
        #print only the even squares from the list
        even_sq = [sq for sq in sq_list if sq % 2 == 0]
        print("Even squares only: {}".format(even_sq))
        
    except Exception as e:
        print("Error occurred: {}".format(e))


# Call function
square()