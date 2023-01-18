"""
Complete the script.
"""""
"""Project 1 - Completing The Script """
"""This script demonstrates Python and it's built-in functions"""
import math

#Create greeting for user and provide instruction
print()
print("Hello, please provide 3 temperatures")
print()
#Get temperatures from user making sure they are of the float data type
temperature_1 = float(input("Please enter a temperature in degrees F: "))

temperature_2 = float(input("Please enter second temperature in degrees F: "))

temperature_3 = float(input("Please provide third temperature in degrees F: "))
print()
"""Let's make sure these temperatures are of the correct data type, we want them to be of the float variety"""
#verify the correct data type for numbers
print(type(temperature_1))
print(type(temperature_2))
print(type(temperature_3))
print()
#Noticing hint provided in instructions and ensuring data is float
print("Are each data types confirmed to be float?")
answer = input("Enter yes or no: ")
print()
print("Thank you for the responses!")
print()
#provide sum of temperatures
print("Here is the sum of your temperatures")
sum = float(temperature_1) + float(temperature_2) + float(temperature_3)
print(round(sum, 2))
print()
#provide average of temperatures
print("Next is the average of your selected temperatures")
average = (sum) / 3
print(round(average, 2))
print()
#provide product of temperatures
print("Here is the product of the temperatures entered")
product = temperature_1 * temperature_2 * temperature_3
print(round(product,2))
print()
#provide min temperature
smallest = min(temperature_1 , temperature_2, temperature_3)
print("This is the smallest temperature in the group")
print(round(smallest, 2))
print()
#provide max temperature
largest = max(temperature_1, temperature_2, temperature_3)
print("This is the largest temperature in the group")
print(round(largest, 2))
print()
#below is where I would list the range, however I was not able to work around an error pertaining to float data being 
#assigned to integer 
print()
"Part 3. Decision Making"
print("This portion of the program will let you know if an entered body temperature requires medical attention or not.")
print("Let's assume you are not sick and have been exposed to extreme cold, or exteme heat.")
number_1 = int(input("Enter a temperature between 91-108 F: ")) 
print()
if number_1 <= 95:
    print("This is a dangerously low body temperature, you may have hypothermia, seek medical attention if you cannot warm up")
if number_1 == 96:
    print("This is a low body temperature, warm up as soon as possible")
if number_1 == 97:
    print("This is a low body temperature, warm up as soon as possible")
if number_1 == 98:
    print("This is a normal body temperature")
if number_1 == 99:
    print("This is a normal body temperature")
if number_1 == 100:
    print("This is a warm body temperature, attempt to cool down")
if number_1 == 101:
    print("This is a warm body temperature, attempt to cool down")
if number_1 == 102:
    print("This is a warm body temperature, attempt to cool down")
if number_1 == 103:
    print("This is a warm body temperature, attempt to cool down")
if number_1 >= 104:
    print("This is a dangerously high body temperature, seek medical attention if you can't cool down")








