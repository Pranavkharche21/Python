#ceate a dictionary and take the input from the user and print the meaning of the word from the dictionary 


print("enter you word")# here the word is taken as a inout from the user 
word = input() # the word enter by the user is stored in word

meaning = {"mutable": "it can be changed","immutable": " it cannot be changed", "set": " it is a collection of data "}
# so i have written the meaning of the word in a dictionary 

print(meaning[word])# here the meaning of the word is printed 
