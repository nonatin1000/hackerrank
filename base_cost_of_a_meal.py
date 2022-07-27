#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = (meal_cost * tip_percent) / 100) + ((meal_cost * tax_percent) / 100)
    total_cost = meal_cost + ((meal_cost * tip_percent) / 100) + ((meal_cost * tax_percent) / 100)
    total_cost = meal_cost + ((meal_cost * tip_percent) / 100) + ((meal_cost * tax_percent) / 100)
    return math.trunc(total_cost)


print(solve(12.00, 20, 8))