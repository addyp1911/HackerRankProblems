import math
import os
import random
import re
import sys
import ast

# Complete the hourglassSum function below.
def hourGlassSum(arr):
    max_total = -99999
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            total = 0
            total += arr[i][j] + arr[i][j+1] +arr[i][j+2] + arr[i+1][j+1]+ arr[i+2][j]+arr[i+2][j+1] + arr[i+2][j+2]
            max_total = max(total, max_total)
    return max_total

if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    hourGlassSum = hourGlassSum(input_lst)
    print(hourGlassSum)