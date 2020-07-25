def alternating_characters(t):
    count = 0
    for i in range(1,len(t)):
        if t[i] == t[i-1]:
                count += 1
    return count

if __name__ == '__main__':

    string_1 = input("Enter a string = ")
    res_count = alternating_characters(string_1)
    print(res_count)
