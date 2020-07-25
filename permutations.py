import ast
def permute(arr):
    if len(arr) == 1:
        return [arr]
    if len(arr) == 0:
        return []
    l = []   
    for i in range(len(arr)): 
        m = arr[i]
        remlst = arr[:i] + arr[i+1:]
        for p in permute(remlst):
            l.append([m]+p)
    return l

if __name__ == '__main__':

    input_lst = ast.literal_eval(input("Enter the array of integers = "))
    permute = permute(input_lst)
    print(permute)    