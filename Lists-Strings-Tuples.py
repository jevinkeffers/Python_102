"""
In this lesson, you will build a simple to-do list program that lets you:

Print your to-do list
Add items to your to-do list
Mark items as "complete" - removing them from the list
"""

"WHAT IS A SEQUENCE?"
"In Python, a sequence is a data type that can store multiple, individual values. Examples of sequences include:"


"List"
programming_languages = ["bash", "Python", "HTML", "CSS", "JavaScript", "SQL"]
#Lists are mutable (modifiable) in sequences - versatile, general-purpose collection.

"Tuple"
gps_coordinates = (33.848673, -84.373313)
#Tuples are immutable sequences - best for representing something with a fixed size (e.g. GPS coordinations)

"Range"
numbers_from_zero_to_a_million = range(1000000)
#Ranges are lists of numeric values

"""
HOW DO I CREATE A LIST?
Lists can hold any other type (Strings, numbers, other Lists, etc.). The easiest way to create one is to assign a List literal to a variable:
"""
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
"""
A List literal is:
• one or more values (or variables)
• separated by commas ,
• enclosed in square brackets []
""" 

"""
HOW DO I ACCESS ITEMS IN A SEQUENCE?
You can access items in a sequence in groups or individually.

#How do I access individual items in a Sequence?
Here is how Python stores values in our todos List:
index   value
0       "pet the cat"
1       "go to work"
2       "feed the cat"

Python uses an integer index to identify values within a single List. 
The first index is always 0.
"""

#You use the index to reer to a specific item in the list:

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

first_item = todos[0]
second_item = todos[1]

# It is not necessary to create a variable. You can index as part of an expression:

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# first_item = todos[0]
print("The first item is:", todos[0])
# second_item = todos[1]
print("The second item is:", todos[1])

"""
Why is a negative index valid?
Python allows you to use a negative index, which tells it to start from the end instead of the beginning.
"""
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

print("This is the last item:", todos[-1])
print("This is the next to last item:", todos[-2])

"""
How do I access groups of items in a Sequence?
You can access all of the items simply by using the variable name for the sequence itself:
"""

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

print("Here are your todos:")
print(todos)

#Which prints 
Here are your todos:
['pet the cat', 'go to work', 'feed the cat']

"You can use the slicing syntax to access a subset of the items:"
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

print("Here are the second and third todos:")
print(todos[1:3]) 

"""
When you slice a List, you normally provide two number separated by a :

The first number is the starting index. It is included in the result
The second number is the ending index. It is not included in the result.
If you omit the starting index, Python starts the slice at the beginning (index 0). If you omit the ending index, Python goes to the end (the last index).

"""

#Here is the output
Slice from the third through the end:
['shop for groceries', 'go home', 'feed the cat']
Slice from the beginning up to, but not including the fourth:
['pet the cat', 'go to work', 'shop for groceries']

# You can use negative indexes with slices:

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

print("Two items up to, but not including the last:", todos[-3:-1])
print("These are the last 3 items:", todos[-3:])

# Which gives the following result:

Two items up to, but not including the last: ['shop for groceries', 'go home']
These are the last 3 items: ['shop for groceries', 'go home', 'feed the cat']


#ITERATING THROUGH A SEQUENCE

"""
Now that you know how to access items manually, it is time to automate that with a loop. Using a loop to access a sequence's items one at a time is called iteration.

In this portion of the lesson, we will print the items of the to-do list.

Recall that a while loop should always move closer to some end condition so that it isn't an infinite loop.

#How do I find the length of a Sequence?
Python provides a len() function that will tell you how many items are in a Sequence.

You give len() a Sequence; it returns an integer. We will use this as part of the condition for a while-loop.
"""

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

index = 0 # Begin with index 0
while index < len(todos):
    todo = todos[index]
    print("%d: %s" % (index + 1, todo))
    index += 1

"""
These are the three parts of our while loop ^ :

• An initial state: we start the index variable at 0
• A condition: only run the code block if index is less than len(todos)
• A code block that moves us closer to the end condition: index += 1

This while-loop is exactly like the simple counter program from the previous lesson. The only difference is that on line 5, we create a todo variable to reference the item at todos[index].

Not only does incrementing move us closer to the end condition, but it lets us access the next item in the list each time the code block runs.

When we run our program, we see the following:
"""
1: pet the cat
2: go to work
3: shop for groceries
4: go home
5: feed the cat

"""
On line 6 of our program, we interpolate the value index + 1 so that it prints a "human readable" version of our index.
"""

"""
What is a for-loop and why should I use it with a List?
Often, you do not need to know the specific index of an item. You just want the items themselves.

Python provides another kind of loop: the for-loop. Here is our to-do printer using this syntax, with the numerical index omitted:
"""
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

for todo in todos:
    print(todo)
"""
It's so much shorter! For-loops are a shorthand for iterating and accessing an item at a time.
"""
pet the cat
go to work
shop for groceries
go home
feed the cat
"""
If you do want to show the index (or at least number the todos) you can add a variable that you display and increment:
"""
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

count = 1
for todo in todos:
    print("%d: %s" % (count, todo))
    count += 1
"""
Other than looking nice next to each to-do, the count variable serves no other purpose in our for-loop.
"""
1: pet the cat
2: go to work
3: shop for groceries
4: go home
5: feed the cat

"""

HOW DO I MODIFY A LIST?

Lists are Python's mutable Sequence type, meaning that you can add, remove, and replace items.

How do I add items to a List?
• There are three ways to add items to a List:

• You can .append() individual items
• You can concatenate two lists together
• You can .extend() a list using elements from another list
• Each List has a .append() method that you can use like this: """

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

todos.append("binge watch a show")
todos.append("go to sleep")

count = 1
for todo in todos:
    print("%d: %s" % (count, todo))
    count += 1

"You can see that it adds on to our original todos:"

1: pet the cat
2: go to work
3: shop for groceries
4: go home
5: feed the cat
6: binge watch a show
7: go to sleep

"Alternatively, you can use the concatenation operator + to combine two lists:"

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
todos = todos + ["binge watch a show", "go to sleep"]
count = 1
for todo in todos:
    print("%d: %s" % (count, todo))
    count += 1

"This is equivalent to using the .extend() method:"

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
todos.extend(["binge watch a show", "go to sleep"])
count = 1
for todo in todos:
    print("%d: %s" % (count, todo))
    count += 1

"""
***

Concatenation produces a new List.

.append() and .extend() modify a List in-place. That is, these mutate a List instead of returning

***

"""
todos = []

# Prompt the user the first time
new_todo = input("What do you need to do? ")
while len(new_todo) > 0:
    todos.append(new_todo)

    # Print the current list of to-do items
    print("To do:")
    print("====================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1

    # Prompt the user again
    print("\n")
    new_todo = input("What do you need to do? ")

print("Have a nice day!")

"""
How do I replace items in a List?

You can use an index to refer to a specific place in a List. If you do this on the LHS of an assignment, you can replace an item:

"""

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
todos[1] = "go to the grocery store"
print(todos)
"In this example, we have reassigned the value at index 1:"
['pet the cat', 'go to the grocery store', 'shop for groceries', 'go home', 'feed the cat']
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

"If you need to replace multiple items, you can use a slice on the LHS and a List on the RHS:"
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
todos[1:4] = ["make cat food", "cook cat food"]
print(todos)
"Here, we replace the items from index 1 up to, but not including index 4:"
['pet the cat', 'make cat food', 'cook cat food', 'feed the cat']
"Notice that our slice on the LHS referred to 3 items, but the List on the RHS only contained 2 items. Python replaces that entire segment of the list with a new list; it is not replacing those items individually."

todos = []

# Create a constant for our main menu.
# This saves us from having to type it out twice.
MAIN_MENU = """
Choose an action:
P: Print your to-do list
A: Add a to-do item
R: Replace a to-do item

(Or press Enter to exit the program.)
"""

choice = input(MAIN_MENU)
choice = choice.upper() # Simplifies our if-conditions

# As long as they type something, keep prompting
while len(choice) > 0:
    if choice == "P":
        # Print the current list of to-do items
        print("\n\n\nTo do:")
        print("====================")
        count = 1
        for todo in todos:
            print("%d: %s" % (count, todo))
            count += 1
    elif choice == "A":
        new_todo = input("What do you need to do? ")
        if len(new_todo) > 0:
            todos.append(new_todo)
    elif choice == "R":
        # Print the current list of to-do items
        print("\n\n\nTo do:")
        print("====================")
        count = 1
        for todo in todos:
            print("%d: %s" % (count, todo))
            count += 1
        
        which_index = input("Which to-do number? ")
        try:
            which_index = int(which_index)
            which_index -= 1 # Convert from human-readable to 0-based index
            
            if which_index >= 0 and which_index < len(todos):
                new_todo = input("What do you need to do? ")
                todos[which_index] = new_todo
        except ValueError:
            print("\n\n***Please enter a number.***") 
    else:
        print("\n\n***Please enter a valid menu option.***")    

    choice = input(MAIN_MENU)
    choice = choice.upper() # Simplifies our if-conditions

print("Have a nice day!")

"""
HOW DO I DELETE ITEMS FROM A LIST

The syntax for removing an item from a List is different from what we've seen so far.
Use the del keyword to tell Python to remove one or more items from a List:

"""

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
del todos[0] # Remove the first one
print(todos)
del todos[1:3] # Remove items at index 1 up but not including index 3
print(todos)
"Here is the output from running the example:"
['go to work', 'shop for groceries', 'go home', 'feed the cat']
['go to work', 'feed the cat']

todos = []

# Create a constant for our main menu.
# This saves us from having to type it out twice.
MAIN_MENU = """
Choose an action:
P: Print your to-do list
A: Add a to-do item
R: Replace a to-do item
C: Complete a to-do item
(Or press Enter to exist the program.)
"""

choice = input(MAIN_MENU)
choice = choice.upper() # Simplifies our if-conditions

# As long as they type something, keep prompting
while len(choice) > 0:
    if choice == "P":
        # Print the current list of to-do items
        print("\n\n\nTo do:")
        print("====================")
        count = 1
        for todo in todos:
            print("%d: %s" % (count, todo))
            count += 1
    elif choice == "A":
        new_todo = input("What do you need to do? ")
        if len(new_todo) > 0:
            todos.append(new_todo)
    elif choice == "R":
        # Print the current list of to-do items
        print("\n\n\nTo do:")
        print("====================")
        count = 1
        for todo in todos:
            print("%d: %s" % (count, todo))
            count += 1
        
        which_index = input("Which to-do number? ")
        try:
            which_index = int(which_index)
            which_index -= 1 # Convert from human-readable to 0-based index
            
            if which_index >= 0 and which_index < len(todos):
                new_todo = input("What do you need to do? ")
                todos[which_index] = new_todo
        except ValueError:
            print("\n\n***Please enter a number.***")
    elif choice == "C":
        # Print the current list of to-do items
        print("\n\n\nTo do:")
        print("====================")
        count = 1
        for todo in todos:
            print("%d: %s" % (count, todo))
            count += 1
        
        which_index = input("Which to-do number? ")
        try:
            which_index = int(which_index)
            which_index -= 1 # Convert from human-readable to 0-based index
            
            if which_index >= 0 and which_index < len(todos):
                completed_todo = todos[which_index]
                del todos[which_index]
                print("%s has been marked complete!" % completed_todo)
        except ValueError:
            print("\n\n***Please enter a number.***")
    else:
        print("\n\n***Please enter a valid menu option.***")    

    choice = input(MAIN_MENU)
    choice = choice.upper() # Simplifies our if-conditions

print("Have a nice day!")

"""
WHEN SHOULD I USE NESTED LOOPS?
Lists can hold any kind of value, including Lists.
You can use nested loops to create nested Lists and to iterate over them.
Let's create a tic-tac-toe board using nested loops. It will look like this:

"""

"""
How do I use the range() function to generate numbers?
To create our game board, we need to produce numbers that correspond to our List indexes.
To do that, we'll use the range() function. You pass range() a number, and it returns the integers up to, but not including that number.
First, let's see the nested loops in action, just printing the numbers generated by range(0):

"""

"""
How do I use Strings as Sequences?
Like Lists, you can index, slice, and get the length of Strings as if though they were Lists. """
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("The first letter is", alphabet[0])

print("The first three letters are", alphabet[:3])

print("Some letters in the middle are", alphabet[11:16])

print("There are %d letters in the alphabet" % len(alphabet))

"""
How do I loop through the characters of a String?
Because you can index and get the length of a String, you can also iterate through the individual characters:
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    print(letter)
"And the results of running the code:"
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z

"""
How do I convert a String into a List?
One notable difference between Strings and Lists is that you cannot modify a String by reassigning to an index. 
You would first have to convert it to a List so that you could mutate the data:
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphalist = list(alphabet)
alphalist[0] = "4"

print(alphalist)
"This allows you to make whatever modifications you choose:"
['4', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
How do I convert a List into a String?
There is a trick to converting your List back into a String, and it is a bit counter-intuitive at first. """
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphalist = list(alphabet)
alphalist[0] = "4"

print(alphalist)

alphabet = "".join(alphalist)
print(alphabet)

# You use the String method .join() to reconnect the items of a List.
# Because we used an empty String ('') to join the items, the resulting String has no spaces:

['4', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
4bcdefghijklmnopqrstuvwxyz

"Note that we did not mutate our String, but did reassign the variable name alphabet to our newly .join()-ed String. But, we can use any String we want to insert between the joined List items:"

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphalist = list(alphabet)
alphalist[0] = "4"

print(alphalist)

alphabet = "!\n".join(alphalist)
print(alphabet)
"Now, our alphabet String has an ! and a line break between each letter:"

['4', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
4!
b!
c!
d!
e!
f!
g!
h!
i!
j!
k!
l!
m!
n!
o!
p!
q!
r!
s!
t!
u!
v!
w!
x!
y!
z

"Note that .join() inserts a String between each List item. The z does not have a ! after it."

"""
What Sequence operations work with Tuples?
Just as with Strings, you can index, slice, and get the length of a Tuple. But you cannot modify a Tuple.
"""

coordinates = (33.848673, -84.373313)

latitude = coordinates[0]
longitude = coordinates[1]

print("The latitude is %f and the longitude is %f" % (latitude, longitude))
This program prints the following:

The latitude is 33.848673 and the longitude is -84.373313

"""
Tuples are immutable.
Assigning to an index of a Tuple results in an error.
But you can concatenate to produce a new Tuple:
"""
band_mates = ("John", "Paul", "George", "Pete")
print(band_mates)

band_mates = band_mates[:-1] # All but the last
print(band_mates)

band_mates = band_mates + ("Ringo", )
print(band_mates)

"This works because you are doing reassignment, not mutation."

('John', 'Paul', 'George', 'Pete')
('John', 'Paul', 'George')
('John', 'Paul', 'George', 'Ringo')"

"To create a Tuple with a single item, you must wrap it in parentheses and add a trailing comma as shown in the previous code sample."

"""
Summary
In this lesson, you learned about the following Sequence types:

Lists
Strings
Tuples
ranges
Sequences in Python share a number of qualities in common. They are all:

index-able
slice-able
length-able
Because of these qualities, they are also iterable (meaning you can use a for-loop with them.)

"""