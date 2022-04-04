def maximum_equalizer(lst):
    initial_list = lst.copy()
    for i in range(1, (len(lst)-1)):
        if (lst[i-1] < lst[i]) and (lst[i] > lst[i+1]):
            if lst[i-1] != initial_list[i-1]:
                lst[i-1] = lst[i]
            else:
                lst[i+1] = lst[i]

    count = 0
    for i in range(len(lst)):
        if lst[i] != initial_list[i]:
            count += 1
    
    print(count)
    print(lst)
             

length = int(input())
in_lst = list(map(int, input().split()))
maximum_equalizer(in_lst)