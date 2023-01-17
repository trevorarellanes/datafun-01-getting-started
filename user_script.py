"""
Complete the script.
"""""
"""Project 1 - Completing The Script """
"""This script demonstrates Python and it's built-in functions"""
import math

#Create greeting for user and provide instruction
print("Hello, please provide 3 temperatures")
print()
#Get temperatures from user making sure they are of the float data type
temperature_1 = float(input("Please enter a temperature in degrees celsius: "))

temperature_2 = float(input("Please enter second temperature in degrees celsius: "))

temperature_3 = float(input("Please provide third temperature in degrees celsius: "))
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
#Although hint from earlier said to use float; this causes an error for calculating range
print("The Range is listed below")
print(range(int(smallest, int(largest))))

"Part 3. Decision Making"









