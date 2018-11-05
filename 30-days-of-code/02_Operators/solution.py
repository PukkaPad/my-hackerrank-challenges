#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    tot = meal_cost + meal_cost*tip_percent/100 + meal_cost*tax_percent/100
    print("The total meal cost is {0:.0f} dollars.".format(tot))