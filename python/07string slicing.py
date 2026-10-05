mystr = "GT650 is a cafe  racer bike"
print(mystr[:5]) # prints the first 5 characters of the string
print(mystr[6:]) # prints the string from index 6 to the end

print(mystr[::2]) # prints every second character of the string
print(mystr[1:10:2]) # prints characters from index 1 to 10 with a step of 2

#some function of string:
print(mystr.upper()) # converts the string to uppercase

print(mystr.lower()) # converts the string to lowercase 

print(mystr.replace("GT650", "Yamaha R15")) # replaces "GT650" with "Yamaha R15"

print(mystr.isalnum()) # checks if the string is alphanumeric (contains only letters and numbers

print(mystr.endswith("bike")) # checks if the string ends with "bike"

print(mystr.count("i")) # counts the number of occurrences of "i" in the string
