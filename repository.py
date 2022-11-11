# repository.py
#
# @ author: N.Yuen20220963
# date: November2022

print('Enter your name:')
x = input()
print('Hello, ' + x)

my_name="Nicola"

#Print my_name:
print"My name is " + (my_name)
print
#Print "Hello World":
print "Hello, World!"
print("Python 3 requires parentheses")
print
#Combine multiple strings:
print "We can combine " + "multiple strings"
print
print"Todays date"
todays_date="8"
print(todays_date)
print
#Arithmetic
days_in_week=7
weeks_in_year=52

days_in_year=(days_in_week)*(weeks_in_year)

print"Days in year"
print(days_in_year)
print
#Divide and print remainder
divide=1398/11
print"Divide"
print(divide)
print
#Divide and print remainder
print"Remainder"
remainder=1398%11
print(remainder)
print
#Updating Variables
fish_in_clarks_pond = 50
 
print "Catching fish"
number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught
print(number_of_fish_caught)
print(fish_in_clarks_pond)

print
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price
print("money_in_wallet")
print(money_in_wallet)

#Updating Variables
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

september_to_december_rainfall=(5.16 + 7.20 + 5.06 + 4.06)
annual_rainfall+=september_to_december_rainfall
print
print("Annual Rainfall")
print(annual_rainfall)