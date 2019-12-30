80#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@title: ps1b.py
@author: John Lewis Jones IV
@date: 15AUG2019
MIT OCW 6.0001
Introduction to Computer Science and Programing in Python
"""
# get the program user's info
anual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-anual raise, as a decimal: '))

# calculate and set variables
portion_down_payment = 0.25 # percent of house to put on down payment
down_payment_amount = total_cost * portion_down_payment
r = 0.04 # anual interest rae on investments
monthly_salary_saved = anual_salary/12*portion_saved # amount of income each month
mr = r/12 # monthly intrest rate on investments

current_savings = 0.00
month = 0

# until you have enough money for the down payment 
while current_savings < down_payment_amount:
    # save money that month
    monthly_ROI = current_savings*mr # Return on Investment each month
    current_savings = current_savings + monthly_ROI + monthly_salary_saved 
    month += 1 # counter
    
    # every 6th month
    if not (month % 6):
        # get a raise
        anual_salary = anual_salary*(1+semi_annual_raise)
        monthly_salary_saved = anual_salary/12*portion_saved
    
print('Number of months:', month)