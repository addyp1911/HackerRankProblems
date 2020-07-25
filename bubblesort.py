import ast
def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps +=1
    firstElement = a[0]
    lastElement =  a[len(a)-1]
    print("Array is sorted in "+ str(numSwaps)+" swaps")
    print("First Element: ", str(firstElement))
    print("Last Element: ",str(lastElement))

if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    countSwaps(input_lst)
