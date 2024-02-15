# insertion
my_dict = {}
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"
print(my_dict)  

# deletion
del my_dict["key1"]
print(my_dict) 

# lookup
val = my_dict.get('key2')
print(val)

# update
my_dict["key2"] ='Kari'
print(my_dict) 
