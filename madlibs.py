# Short Mad Libs Game

print("Welcome to the Mad Libs Game!")
print("Fill in the blanks to complete the story.\n")

# Collect user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
food = input("Enter a type of food: ")

# Story template
story = f"""      
One day, {name} went to {place} for an adventure. 
It was a very {adjective} day, and {name} saw a {animal} that was trying to {verb}.
Surprised, {name} decided to share some {food} with the {animal}, 
and they became best friends. What a day!
"""
#You can create formatted strings that span multiple lines by combining f with triple quotes (""" or ''')

# Display the story
print("\nHere’s your story:")
print(story)