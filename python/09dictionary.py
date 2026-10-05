#dictionary is nothing but key value pairs
dict1 ={"abhshik":"kebab", "raj":"chicken", "sahil":"mutton"}
print(dict1["raj"])
dict1["ankit"] = "fish" 
print(dict1)
dict1["veg"] = "chicken"
print(dict1)
del dict1["veg"]
print(dict1)
dict1.update({"nonveg":"mutton"})
print(dict1)