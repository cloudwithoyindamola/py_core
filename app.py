
#print("Hello world")
#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")

#print ("There was a man named john,")
#print ("he was 35 years old.")
#print ("He really liked the name john,")
#print ("but he didnt like being 35.")

    #VARIABLE
# character_name = "John"
# character_age = 35
# is_male = False
# print (f"There was a man named {character_name} ,")
# print (f"he was {character_age} years old.") 

# character_name = "Mike"

# print (f"He really liked the name {character_name},")
# print (f"but he didnt like being {character_age}.")

# print ("Girraffe\nAcademy")   #prints Academy on a new line
# print ("Girrafe\"Academy")   #means put a quotation mark after Girrafe, becos pottting only the " means we want to end it at Girrafee
# print ("boy\girl")    #means put \after boy

         # STRING VARIABLE
# Phrase = "Giraffe Academy"
# print(Phrase)
# #concatenatiON - putting a string with another string or number
# print(Phrase + " is cool")

    # #Functions
# phrase = "Giraffe Academy"
# print(phrase.lower())      #change to lowercases
# print(phrase.upper())      #change to uppercases
# print(phrase.isupper())     #to check if the string is uppercase

# #double function
# print(phrase.upper().isupper())  #conert to uppercase first then return true 

#LEN FUNCTION - USED TO KNOW THE LENGTH OF A STRING
# phrase = "Giraffe Academy"
# print(len(phrase))

# print (phrase[0])     #prints the speecified position character e.g01234567...

# #index function- tell us where a specific characteris located
# print (phrase.index("G"))   #PRINTS THE POSITION OF G

# #REPLACE FUNCTION
# phrase = "Giraffe Academy"
# print(phrase.replace("Giraffe", "Elephant")
  
     #NUMBER VARIABLE
# print(2)
# print(3 + 5)   #CAN BE +, - , / , * or decimal
# print(3 * (4 + 5))     #do the math in the parenthesis first
# #modulus operator
# print(10 % 3)   #this prints the remainder

#variable
# my_num = 5
# print(my_num)
# # my_num = 5
# # print(f"{my_num} my favourite number")        #same result
# # print(str(my_num) + " my favourite number")   #same result
  
#    #MATH FUNCTIONS

# #ABS- Absolute value
# my_num = -5
# print(abs(my_num))     #prints 5 without the negativesign
 
# #pow function
# print (pow(4, 6))     #means 4to the power of 6

# #max function
# print (max(4, 6))    #returns larger number

# #min function
# print (min(4, 6))    #returns lowest number

# #round function
# print (round(3.6))    #returns round figure

# from math import *    #this is needed to use the below math function
# print (floor(3.6))     #removes the decimal and prints only 3
# print (ceil(3.6))      #always round the numbr up
# print (sqrt(36))       #squareroot of a number

#INPUTTING
# name =input("Enter your name: ")
# age =input("Enter your age: ")
# print(f"welcome {name}! , your are {age} years old")

num1 =input("enter the number:")
num2 =input("enter another number:")
result =float(num1) + float(num2)    #use int for whole decimak only, use float for decimal numbers 

print(f"{result}")