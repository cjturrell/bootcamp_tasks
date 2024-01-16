# A program to continually ask user to input number

# Define variables with value zero to start
sum = 0         
count = 0

# Ask user to input any number. Program will sum and count
num = int(input("Please enter a number: "))     
sum += num      
count += 1     

while num > 0:  # Loop to continually ask user to input numbers
    num = int(input("Please enter another number: "))
    
    if num < 0:  # Stops loop when -1 is input
        break

    sum += num  # Sums users input if not -1
    count += 1  # Total count users input if not -1
     

# Calculate average of numbers entered (not including -1)
avg = sum / count                   
print("The average is: ", avg)  