"""
write code to output pattern. Using if-else statement in combination with a single for loop
*
**
***
****
*****    up to 5 stars
****
***
**
*
"""

# Define variable and counter for iterations
star = '*' 
counter = 0  

# For 9 iterations, print each one and track using counter
for i in range(9):
    print(star)
    counter += 1
    
    # If less than 5, add one star each iteration
    if counter < 5:
        star += '*'

    # When 5 reached, remove one star each iteration
    else:
        star = star[:-1]