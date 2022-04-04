def khosh_tarif(str):
    
    for i in range(len(str)-1):         # cheks if the input string contains two similar neighbor digits
        if ((str[i] == '0') and (str[i+1] == '0')) or ((str[i] == '1') and (str[i+1] == '1')):
            return('Bad tarif')
        else:
            continue
    
    tmp1 = '0'                          # creates two desired patterns with the same length as input string, tmp1 begins with '0' and tmp2 begins with '1'
    tmp2 = '1'
    for i in range(len(str)-1):
        if tmp1[i] == '0':
            tmp1 += '1'
            tmp2 += '0'
        else:
            tmp1 += '0'
            tmp2 += '1'
    
    flag = False
    for i in range(len(str)):           # compares and matches the input string's characters to tmp1
        if str[i] != '?':
            if str[i] == tmp1[i]:
                flag = True
            else:
                flag = False
                break

    if flag == True:
        return('Khosh Tarif')
    else:
        for i in range(len(str)):       # compares and matches the input string's characters to tmp2
            if str[i] != '?':
                if str[i] == tmp2[i]:
                    continue
                else:
                    return('Bad tarif')
        return('Khosh Tarif')
            

in_str = input()
print(khosh_tarif(in_str))