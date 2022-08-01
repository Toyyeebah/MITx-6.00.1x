#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:44:46 2022

@author: toyyeebahmustapha
"""
"""
Background 
In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and
clearly you are going to be worth more to your company over time! So we are going to build on your
solution to Part A by factoring in a raise every six months. 
In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
your program to include the following:
    
1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18  month, and so on. 

Write a program to calculate how many months it will take you save up enough money for a down
payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).  

Have the user enter the following variables:
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)

SOLUTION

The solution to this problem is essentially the same as the solution to problem set A with one small change. 
They say that you are getting a raise every six months.

You can easily calculate the raise by adding the extra money to the salary variable, 
but you need to do this only every six months.

The % operator gives returns remainders. Whenever the remainder of 6 is zero you are going to know that 
that number is a multiple of 6. You can add this condition in as an if statement into the while loop.

"""
#user input
annual_salary = float(input("Enter your starting annual salary: "))  #annual salary
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))    # % of savings from salary each month
total_cost = float(input("Enter the cost of your dream home: "))     #($), total cost of dream house
semi_annual_raise = float(input("Enter a semi-annual raise, as a decimal: "))

#Variables definition
portion_down_payment = 0.25 * total_cost            #equired down payment percentage 
current_savings = 0                                 #($), amount saved thus far
r = 0.04                                            #annual rate
annual_return = (current_savings * r) / 12          #return on savings
monthly_salary = annual_salary/12
portion_saved = portion_saved * monthly_salary


#computational Output
months = 0
while (current_savings <= portion_down_payment):
    
    current_savings += (current_savings * r / 12) + portion_saved    
    months += 1
    if months%6 == 0:
        monthly_salary = (semi_annual_raise * monthly_salary) + monthly_salary 
        portion_saved = monthly_salary * portion_saved   
print('Number of months: ', months)