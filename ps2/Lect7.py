#!/usr/bin/env python3
""" Lecture 7 Notes """

# Modular code is better code. 
# Defensive programing.
# Make everything testable, modular, and easier to debug.

# 1) Ensure code runs
# 2) Create some test cases
#   - Unit Testing: making sure each function runs acording to the specification
#   - Regression Testing: test for bugs as you find them
#   - Integration Testing: Does the overall program work?

# Testing Approaches
#   Natural bondaries of the problem from the doc string
#   Black box testing - based off specifications
#   Glass box testing - based off exhausting all paths/branches through the code 
#     branches
#       excercise all parts of a conditional
#     for loops
#       1. loop not entered
#       2. body of loop executred exactly once
#       3. body of loop executed more than once
#     while loops
#       same as for loops, & cases that catch all ways to exit loop

"""
EXAMPLES 
"""

def abs(x):
  """ Assuems x is an int
  Returns x if x>= 0 and -x otherwise """
  if x < -1:
    return -x
  else:
    return x

def sqrt(x, eps):
  """ Assume x, eps floats, x >= 0, eps > 0
  Returns res such that x-eps <= res*res <= x+eps """
  pass

  
