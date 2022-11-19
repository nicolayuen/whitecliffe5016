#STRING TYPES
print("STRING TYPES")
print("")

#Use ord() to covert letters to numbers 
#Converts letter A to 65
convert=ord('A')
print("Convert letter A to number 65")
print(convert)
print("")

#Creates a int containing value 123
print("Create an int containing value 123")
my_int=int("123")
print("")
print(my_int)
print("")

#Creates a float containing value 321
print("String types. Create an float containing value 123")
my_float=float("321")
print("")
print(my_float)
print("")

#USES OF BOOLEAN VALUES
print("USES OF BOOLEAN VALUES")
print("")

#Use type() to see the type of a variable
print("See the type of variable")
this_bool=1>2
print(this_bool)
print("")
#Returns false because 1 is not greater than 2

#Boolean values
print("Places 16 in this_int and find the data type")
this_int=16
output=type(this_int)

print(output)
print("returns int because it contains an int value")
print("")

#Creates a random integer. If false, returns Annabelle, if true, returns Rangi.
import random
 
male = False
male = bool(random.randint(0, 1))
 
if (male):
   print ("We will use name Rangi")
else:
   print ("We will use name Annabelle")

print(male)

print("Annabelle is false and Rangi is true")

print("Randint returns a random number and bool converts to boolean values")
print("")

#Creates random integer
print("Creates random integer")
random_integer=(random.randint(0, 1))
print(random_integer)
print("")

#Bool converts number to true or false
print("Converts to true or false")
covert_random_integer=bool(random_integer)
print(covert_random_integer)
print("")

#Boolean
print("0 is false")
false_boolean_number=0
print(bool(false_boolean_number))
print("")
print("1 is true")
true_boolean_number=1
print(bool(true_boolean_number))
print("")

print("Any integer returns True")
a=1
b=2
c=3
print(bool(a))
print(bool(b))
print(bool(c))