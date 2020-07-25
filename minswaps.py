import ast
def minimumSwaps(arr):
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] != i+1:
            while(arr[i] != i+1):
                temp = 0
                temp = arr[arr[i]-1]
                arr[arr[i]-1]= arr[i]
                arr[i] = temp
                count +=1
        i+=1
    return count

if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    minimumSwaps = minimumSwaps(input_lst)
    print(minimumSwaps)
