"""
    =========== Exercise 1 =============

    Using a list, create a shopping list of 5 items. Then
    print the whole list, and then each item individually.

shopping_list = ["rice", "milk", "chicken", "apples", "bread"] # Fill in with some values

print(shopping_list) # Print the whole list

print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4]) # Figure out how to print individual values


    =========== Exercise 2 =============

    Find something that you can eat that has nutrition
    facts on the label. Fill in the dictionary below with
    the info on the label and try printing specific information.

    If you can't find anything nearby you can use this example: https://www.donhummertrucking.com/media/cms/Nutrition_Facts_388AE27A88B67.png

When ready to work on these exercises uncomment below code

nutrition_facts = {
    "Energy" : "1591Kj",
    "Fat" : "13.2g",
    "Fibre" : "1.7g",
    "Protein" : "5.3g",
    "Salt" : "0.4g"
} 

# Fill in with the nutrition facts from the label

print(nutrition_facts) # Print all the nutrition facts

print(nutrition_facts["Salt"]) # Uncomment this line and pick a value to print individually


    =========== Exercise 3 =============

    Python has a function built in to allow you to
    take input from the command line and store it.

    The function is called input() and it takes one
    argument, which is the string to display when
    asking the user for input.


    Here is an example:
    ```
    >> name = input('What is your name?: ')

    >> print(name)
    ```

    Using the information about type casting take an input
    from the command line (which is always a string), convert
    it to an int and then double it and print it.

    i.e. if the user provides 21 then the program should print 42
"""

# When ready to work on these exercises uncomment below code

age = input('What is your age?: ')

print (int(age) * 2 ) # Find a way to convert the age to an int and multiply by 2

