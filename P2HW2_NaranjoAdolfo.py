num1 =  int( input('Enter a budget please: '))

travel_destination = input('Travel destination: ')

num2 = int( input('Gas: '))

num3 = int( input('Accomodation: '))

num4 = int( input('Food: '))

expenses = num2 + num3 + num4

remaining_balance = num1 - expenses

# This program calculates and displays travel expenses
# 04/06/2023
# CTI-110 P1HW1-Travel 
# Adolfo Naranjo


print('This program calculates and displays travel expenses')
print('Enter Budget:', num1)
print()
print('Enter your travel destination:', travel_destination)
print()
print('How much do you think you will spend on gas?', num2)
print()
print('Approximately, how much will you need for accomodation/hotel?', num3)
print()
print('Last, how much do you need for food?', num4)
print()
print('----------Travel Expenses----------')
print('Location:', travel_destination)
print(f"{'Initial Budget:' : <20}", f"{ '$'+str(float(num1)) : <20}")
print(f"{'Fuel:' : <20}", f"{'$'+str(float(num2)) : <20}")
print(f"{'Accomodation:' : <20}", f"{'$'+str(float(num3)) : <20}")
print(f"{'Food:' : <21}" f"{'$'+str(float(num4)) : <21}")
print()
print(f"{'Remaining Balance:': <21}" f"{'$'+str(float(remaining_balance)) : <21}")
