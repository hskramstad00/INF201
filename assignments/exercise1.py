# Task 1
# A program that asks for the users name and prints out a greeting
print('task 1:')
name = input("Please enter your name: ")

print(f'Welcome to INF201 {name}')
print()
# Task 2
# A pretty greeting
# Write a program to place a greeting into the frame from task 1. 
# Width of the frame adapts to the length of the name
print('task 2:')
name_task_2 = input("Please enter your name: ")
print()
lenght_name = len(name_task_2)
formating_top = "*" * (lenght_name + 24)
print(formating_top)
print(f'* Welcome to INF201 {name_task_2} *')
print(formating_top)