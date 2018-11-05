#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print(max([(len(l)) for l in bin(n)[2:].split("0")]))