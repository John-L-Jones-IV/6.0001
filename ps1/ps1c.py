#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@title: ps1c.py
@author: John Lewis Jones IV
@date: 15AUG2019
MIT OCW 6.0001
Introduction to Computer Science and Programing in Python

A simple program to calculate how much needs to be saved
per month in order to reach a savings goal
"""
starting_salary = int(input('Enter the starting salary: '))

semi_anual_raise = 0.07 # 7% pay raise every six months
r = 0.04 # montly roi on saved investments
down_payment_amount = 1000000.0*0.25

min_rate = 0
max_rate = 10000
search_cnt = 0

# make sure it is possible to save for the down payment
if (3*starting_salary < down_payment_amount):
    worth_while = False
    print('It is not possible to pay the down payment in three years.')
else:
    worth_while = True

# if possible and until we have found the correct savings percent
while worth_while:
    search_cnt += 1 # incriment search counter
    guess = (min_rate + max_rate) // 2 # strategically guess center of possible range
    percent_saved = guess/10000.0 # float conversion
    
    # reset to post-graduation condidtions
    current_savings = 0.00
    anual_salary = starting_salary
        
    # simulate 36 months
    for month in range(1,37): # 1-36 months
        monthly_salary_saved = anual_salary/12*percent_saved
        current_savings += monthly_salary_saved + current_savings*r/12
        if (month % 6 == 0): # every 6 months after starting
            anual_salary *= 1+semi_anual_raise
            
    # evaluate the 36 months
    if (min_rate == max_rate):
        print('resolution too course in bisection search...')
        break
    elif current_savings > down_payment_amount + 100:
        max_rate = guess   
    elif current_savings < down_payment_amount - 100:
        min_rate = guess
    else:
        print('Best savings rate:', percent_saved)
        print('Steps in bisection search:', search_cnt)
        break   