def list_comparison(list1,list2):
    y = 0
    common_list = []
    tmp1 = []
    tmp2 = []
    for i in range(len(list1)):
        if i+1 < len(list1):
            if list1[i+1] > list1[i]:
                tmp1.append(list1[i])
                continue
            else:
                tmp1.append(list1[i])
        else:
            tmp1.append(list1[i])
        
        for j in range(y,len(list2)):
            if j+1 < len(list2):
                if list2[j+1] > list2[j]:
                    tmp2.append(list2[j])
                    continue
                else:
                    tmp2.append(list2[j])
                    y = j+1
                    break
            else:
                tmp2.append(list2[j])
                
        for k in tmp2:
            if k in tmp1:
                common_list.append(k)
        
        tmp1 = []
        tmp2 = []

    return common_list

print(list_comparison([1,3,8,12,24,2,15,16,21],[1,8,9,21,2,16]))
        
