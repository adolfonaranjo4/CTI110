#CTI-110
#P3HW2 - Salary
#Adolfo Naranjo
#04-21-2023

employee_name = input("Enter employee's name: ")
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    over_time = hours_worked - 40             
    reg_pay = pay_rate * 40
    ot_payrate = pay_rate + (pay_rate * 0.5)
    overtime_pay = over_time * ot_payrate

else:
    reg_pay= hours_worked * pay_rate


gross_pay = reg_pay + overtime_pay

print("Enter employee's name:, employee_name")
print("Enter numberof hours worked:, hours_worked")
print("Enter employee's pay rate:, pay_rate")
print('-------------------------------------------')
print('Employee name:, employee_name')
print()
print('Hours Worked   Pay Rate    OverTime    OverTime Pay       RegHour Pay        Gross Pay')
print('-------------------------------------------------------------------------------------------------')
print(f'{hours_worked:<15.1f}{pay_rate:<15.2f}{over_time:<15.1f}{ot_payrate:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')
print(f'{hours_worked:<15.1f}{pay_rate:<15.2f}{over_time:<15.1f}{ot_payrate:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')      



                 
                 
                 
                 

             
