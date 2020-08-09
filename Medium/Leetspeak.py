# Given a paragraph of text as a String, print the paragraph in leetspeak.
# To translate a String to leetspeak, you need to make the following character replacements (treat all input characters as uppercase):

# A -> 4 
# E -> 3
# G -> 6 
# I -> 1
# O -> 0
# S -> 5
# T -> 7

# Example: If your program is given the String "I am a leet programmer", it should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation


leet_string = "To translate a String to leetspeak, you need to do the following character replacements: A, E, G, I , O, S, T"
leet_string = leet_string.replace('a', '4')
leet_string = leet_string.replace('A', '4')
leet_string = leet_string.replace('e', '3')
leet_string = leet_string.replace('E', '3')
leet_string = leet_string.replace('g', '6')
leet_string = leet_string.replace('G', '6')
leet_string = leet_string.replace('i', '1')
leet_string = leet_string.replace('I', '1')
leet_string = leet_string.replace('o', '0')
leet_string = leet_string.replace('O', '0')
leet_string = leet_string.replace('s', '5')
leet_string = leet_string.replace('s', '5')
leet_string = leet_string.replace('t', '7')
leet_string = leet_string.replace('T', '7')
print(leet_string)

new_leet_string = "Da doy dought da dasketdall."
new_leet_string = new_leet_string.replace('a', '4')
new_leet_string = new_leet_string.replace('A', '4')
new_leet_string = new_leet_string.replace('e', '3')
new_leet_string = new_leet_string.replace('E', '3')
new_leet_string = new_leet_string.replace('g', '6')
new_leet_string = new_leet_string.replace('G', '6')
new_leet_string = new_leet_string.replace('i', '1')
new_leet_string = new_leet_string.replace('I', '1')
new_leet_string = new_leet_string.replace('o', '0')
new_leet_string = new_leet_string.replace('O', '0')
new_leet_string = new_leet_string.replace('s', '5')
new_leet_string = new_leet_string.replace('s', '5')
new_leet_string = new_leet_string.replace('t', '7')
new_leet_string = new_leet_string.replace('T', '7')
print(new_leet_string)

#Surely there's a cleaner way to do this, but SOLVED