import ast
def diagonalDifference(arr):
    sum_1 = sum_2 = 0
    for i in range(len(arr)):
        sum_1 += arr[i][i]
        sum_2 += arr[i][len(arr)-1 -i]
    return abs(sum_1 - sum_2)    


if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    diagonal_diff = diagonalDifference(input_lst)
    print(diagonal_diff)
