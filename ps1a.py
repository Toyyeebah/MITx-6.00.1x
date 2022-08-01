#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:44:29 2022

@author: toyyeebahmustapha
"""


"""
This codes introduce you to using control flow in Python and formulating
a computational solution to a problem. 

QUESTION

Part A: House Hunting
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:
1. Call the cost of your dream home ​ total_cost​ .
2. Call the portion of the cost needed for a down payment ​ portion_down_payment​ . For
simplicity, assume that portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far ​ current_savings​ . You start with a current
savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of ​ r ​ (in other words,
at the end of each month, you receive an additional ​ current_savings*r/12​ funds to put into
your savings – the 12 is because ​ r ​ is an annual rate). Assume that your investments earn a
return of r = 0.04 (4%).
5. Assume your annual salary is ​ annual_salary​ .
6. Assume you are going to dedicate a certain amount of your salary each month to saving for
the down payment. Call that ​ portion_saved​ . This variable should be in decimal form (i.e. 0.1
for 10%).
7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your ​ monthly salary ​ (annual salary / 12).

TASK

Write a program to calculate how many months it will take you to save up enough money for a down
payment. You will want your main variables to be floats, so you should cast user inputs to floats.   

Your program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)

Try different inputs and see how long it takes to save for a down payment.  Please make your
program print results in the format shown in the test cases below.   
Test Case 1 
>>>
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183 
>>>
Test Case 2 
>>>
Enter your annual salary: 80000 
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
"""

#input values
annual_salary = float(input("Enter your annual salary: "))  #annual salary
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))    #% of savings from salary each month
total_cost = float(input("Enter the cost of your dream home: "))     #total cost of dream house

#Variables definition
portion_down_payment = (0.25 * total_cost)          #required down payment percentag 
current_savings = 0                                 #($), amount saved thus far
r = 0.04                                            #annual interest rate 
annual_return = (current_savings * r) / 12          #return on savings
monthly_salary = annual_salary/12
portion_saved = portion_saved * monthly_salary


#computational Output
months = 0
while current_savings <= portion_down_payment:
    months += 1
    current_savings += current_savings * (r / 12) + portion_saved    
print('Number of months: ', months)