"""
A program to read a string that alternates lower case and upper case letters 
in the output Eg 'Hello World' outputs 'HeLlO WoRlD'
Then outputs alternative words in lower and upper case
Eg 'i am learning to code' outputs'i AM learning TO code
'"""

# User to enter any word or sentence until 'stop' entered
while True:
    user_input = input("Enter any word or sentence (type stop to end): ")
    print("Your input is: " + str(user_input))

    if user_input == "stop": 
        break

    upper_and_lower = ""
    
    # For even index characters-change to uppercase. odd-change to lowercase
    for i in range(len(user_input)):  
        if i % 2 == 0:
            upper_and_lower += user_input[i].upper()
        else:
            upper_and_lower += user_input[i].lower()

    print("Alternating upper and lower case characters: " + str(upper_and_lower))

    # List input using split to then iterate through
    input_list = user_input.split()
    # print("The string as a list is : ", input_list)
    
    alt_case_words = []  

    # For even idex element in list - add to new list as uppercase.  
    # If odd -  add to new list as lowercase
    for j in range(len(input_list)): 
        if j % 2 == 0:
            alt_case_words.append(input_list[j].upper())
        else:
            alt_case_words.append(input_list[j].lower())
   
    # Use join to print as string not list
    print("Alternating upper and lower case words: " + str(" ".join(alt_case_words)))
