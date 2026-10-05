grocery = ["vimbar", "powder","tea","sugar","salt"]
print(grocery[:4])

numbers = [1, 9, 3, 4, 9]
print(numbers[1:4]) # Output: [9, 3, 4]
print(numbers.sort())# Output: None
numbers.sort()
print(numbers) # Output: [1, 3, 4, 9, 9]
numbers.reverse() 
print(numbers) # Output: [9, 9, 4, 3, 1]

#some python function
numbers = [2,3,4,7]
numbers.append(8) 
print(numbers) # Output: [2, 3, 4, 7, 8]
#append function is used to add an element at the end of the list 
numbers.insert(2,5)
print(numbers) # Output: [2, 3, 5, 4, 7, 8]
# insert function is used to insert an element at a specific index in the list 
numbers.remove(8)
print(numbers) # Output: [2, 3, 5, 4, 7]
#some python function

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
##count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#sort()	    Sorts the list

#mutable - that are changeable after creation. Lists are mutable, meaning you can change their content without changing their identity. You can add, remove, or modify elements in a list.
#immutable - that cannot be changed after creation. Tuples are immutable, meaning once they are created, their content cannot be altered. You cannot add, remove, or modify elements in a tuple.

# in short we can say tha 
#mutable - can change 
#immutable - cannot change
