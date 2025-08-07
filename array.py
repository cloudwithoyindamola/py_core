#An array is like a container or a list that holds multiple values in one variable, instead of creating a separate variable for each item.

 #defining and declaring an array
arr = [10, 20, 30, 40, 50]
#print (arr)
 #accessing arraYS
print(arr [0])
print(arr [1])
print(arr [2])
print(arr [-1])
print(arr [-2])

brands = ["coke", "toyota", "apple", "microsoft", "google"]
print (brands)

 #finding length of an array
num_brands = len(brands)
print (num_brands)

 #adding an element to an array using append()
brands.append("intel")
print (brands)

 #removing element from array
del brands[4]
print(brands)
#or use this by specifying directly
brands.remove("microsoft")
print(brands)
#
brands.pop(3)
print(brands)

 #modyfying elements of an array using indexing (replacing an element with another elemet)
fruits = ["Apple", "Banana", "Carrot", "Dates", "Fezli"]
fruits [1] = "Guava"  #REPLACES the no1 element with NVIDA
print(fruits)
fruits [-1] = "Guava"  #REPLACES the last element with NVIDA
print(fruits)
 
 #Concatenating to arrays using the + operator
concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

 #Repeating elements in an array
repeat = ["a"]
repeat = repeat * 6
print(repeat)

 #slicing an array
fruit = ["Apple", "Banana", "Carrot", "Dates", "Fezli"]
print(fruit[1:4])
print(fruit[ :3])
print(fruit[-4: ])
print(fruit[-3:-1])

 #declaring and defining multi-dimensional array
multd = [[1,2], [3,5], [6,9]]
print (multd [0])
print (multd [1])
print (multd [2])
print (multd [2][1])
print (multd [0][0])