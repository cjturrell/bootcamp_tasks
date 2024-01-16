# A program that replaces character, converts to upper case and reverses a string

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

sentence2 = sentence.replace("!", " ")  # Replace '!' with a space

print(sentence2)  # Print with space instead of !
print(sentence2.upper())  # Print in UPPER CASE
print(sentence2[::-1])  # Print in reverse

