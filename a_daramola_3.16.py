#Akinola Daramola Jr
#Programming Exercise 3.16
#Due 06/23/2022

"""
February Days
The month of February normally has 28 days. But if it is a leap year, February has 29 days. Write a program that asks the user to enter a year. The program should then display the number of days in February that year. Use the following criteria to identify leap years:
Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
 
If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.
 
Here is a sample run of the program:
 Enter a year: 2008  [Enter]  In 2008 February has 29 days.
"""

#Initializing value of year variable
year = 0

#Declaring value of variable
year = int(input("Enter a year: "))


#Conditional Statements

#Year divisible by both 100 & 400
if year % 100 == 0 and year % 400 == 0:
    print(f"In {year} Feburary has 29 days. This is LEAP YEAR!")
#Year not divisible by 100 but divisible by 4    
elif not year % 100 == 0 and year % 4 == 0:
    print(f"In {year} Feburary has 29 days. It is a leap year")
#Default statement
else:
    print(f"In {year} Feburary has 28 days. It is not a leap year")
