def change_pattern(input_list):
    counter = 0 
    for i in range(2,len(input_list)):
        if input_list[i-1] > input_list[i-2]:
            if input_list[i] > input_list[i-1]:
                continue
            else:
                counter += 1
        elif input_list[i-1] < input_list[i-2]:
            if input_list[i] < input_list[i-1]:
                continue
            else:
                counter += 1
    return counter

print(change_pattern([1,8,12,3,4,9,2,5,9,7,15]))