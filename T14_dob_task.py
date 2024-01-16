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


"""Using open/close instead of with/as"""
# # Open txt file and get 1st and 2nd string data for each line
# info = open('DOB.txt', 'r')
# print("\033[1m" + "\nName" + "\033[0m")
# for line in info:
#     name = line.strip()
#     name = line.split()
#     print(name[0], name[1])

# # Open txt file and get 3rd, 4th and 5th string data for each line
# info.seek(0)
# print("\033[1m" + "\nBirthdate" "\033[0m")
# for line in info:
#     dob = line.strip()
#     dob = line.split()
#     print(dob[2], dob[3], dob[4])

# info.close()



# lines = file.readlines()

# info = open('DOB.txt', 'r')
# dob_read = info.readlines()
# # would need to split each string in list then call on first and second index for each string
# for i in dob_read:
#     print(dob_read[0], dob_read[1])



# print("\033[1m" + "\nName" + "\033[0m")
# for line in info:
#     name = line.strip()
#     name = line.split()
#     print(name[0], name[1])

# # Open txt file and get 3rd, 4th and 5th string data for each line
# info = open('DOB.txt', 'r')
# print("\033[1m" + "\nBirthdate" "\033[0m")
# for line in info:
#     dob = line.strip()
#     dob = line.split()
#     print(dob[2], dob[3], dob[4])

# info.close()


try: 
    with open('DOB.txt', 'r') as info:
        print("\033[1m" + "\nName" + "\033[0m")
        for line in info:
            name = line.strip()
            name = line.split()  # Each string as a list
            print(name[0], name[1])

        # Open txt file and get 3rd, 4th and 5th string data for each line
        info.seek(0)
        print("\033[1m" + "\nBirthdate" "\033[0m")
        for line in info:
            dob = line.strip()
            dob = line.split()
            print(dob[2], dob[3], dob[4])
except FileNotFoundError:
    print("File not found, check folder")
finally:
    info.close()
 # CHECK GIT HUB CODE FOR THIS