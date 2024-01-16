"""
A program that asks user to input times for their triathlon 
Output based on total time and which category
"""

# User inputs time for each of the 3 tri events
swim = float(input("What was your time for swimming in minutes?"))
cycle = float(input("What was your time for cycling in minutes"))
run =  float(input("What was your time for running in minutes?"))

# Sum and print total time for triathlon
total_time = swim + cycle + run
print(f"You completed the triathlon in {total_time} minutes") 

# Qualifying time ranges applied to total time
if total_time <= 100:
    print("You are in the qualifying time, you got Provincial Colors!")
elif (total_time > 100) and (total_time <= 105):
    print("you are within 5 minutes of qualifying time, you got Provincial Half Colors.")
elif (total_time > 105) and (total_time <= 110):
    print("You are within 10 minutes of qualifying time, you got Provincial Scroll.")
else:  # If 111 minutes or more
    print("You are more than 10 minutes over qualifying time. No award.")