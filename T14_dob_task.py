"""
Program to import information from text file
print names and then date of births
"""

# Checks which directory/folder is open for accessing files correctly
import os
print(os.listdir())

# Open txt file and get 1st and 2nd string data for each line
with open('DOB.txt', 'r') as info:
    print("\033[1m" + "\nName" + "\033[0m")
    for line in info:
        name = line.strip()
        name = line.split()  # Each string as a list
        print(name[0], name[1])

# Open txt file and get 3rd, 4th and 5th string data for each line
with open('DOB.txt', 'r') as info:
    print("\033[1m" + "\nBirthdate" "\033[0m")
    for line in info:
        dob = line.strip()
        dob = line.split()
        print(dob[2], dob[3], dob[4])


"""Using try/except and also open/close instead of with/as """
try:
    # Open txt file and get 1st and 2nd string data for each line
    info = open('DOB.txt', 'r')
    print("\033[1m" + "\nName" + "\033[0m")
    for line in info:
        name = line.strip()
        name = line.split()
        print(name[0], name[1])

#     # Open txt file and get 3rd, 4th and 5th string data for each line
#     info.seek(0)
#     print("\033[1m" + "\nBirthdate" "\033[0m")
#     for line in info:
#         dob = line.strip()
#         dob = line.split()
#         print(dob[2], dob[3], dob[4])

except FileNotFoundError:
    print("File not found, check folder")

# finally:
#     info.close()