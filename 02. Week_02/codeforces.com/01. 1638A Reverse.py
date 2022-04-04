n = int(input())
         
for i in range(n):
    l = 0
    r = 0
    list1_length = int(input())
    list1 = list(map(int, input().split()))
            
    if list1_length == 1:
        print(list1[0])
        continue
            
    for j in range(list1_length):
        if list1[j] == j+1:
            continue
        else:
            l = j
            for k in range(j+1,list1_length):
                if list1[k] == j+1:
                    r = k
                    break
            break

    if r:
        list1[l:r+1] = list1[l:r+1][::-1]
         
    for j in list1:
        print(j, end=' ')
    print()
    