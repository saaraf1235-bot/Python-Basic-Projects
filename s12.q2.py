def analyze_string(str):
    #handling empty string case
    if not str:
        print("Error:Empty string.Please provide some text.")
        return
    
    #print length using len()
    print("Length of string: ",len(str))

    #print string in reverse using slicing
    print("Reversed string: ",str[::-1])

    #counting voewls - case sensitive
    vowels = "aeiou"
    count_vowel = 0
    for char in str.lower():  #converting to lowercase
        if char in vowels:
            count_vowel += 1
            print(f"Number of vowels: {count_vowel}")

    #for loop with range() to print each char with positive and negative index
    print("\nCharacter | Positive index | Negative index")
    for i in range(len(str)):
        positive_index = i
        negative_index = i-len(str) 
        print(f"{str[i]} | {positive_index} | {negative_index}")

#calling function with user input
s = input("Enter string to analyze:")
analyze_string(s)