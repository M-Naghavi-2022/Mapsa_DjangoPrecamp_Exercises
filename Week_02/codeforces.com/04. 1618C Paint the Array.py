r = int(input())
for i in range(r):
    n = int(input())
    a = list(map(int, input().split()))
    for j in range(1, min(a)+1):
        l = []
        for k in a:
            if k%j == 0:
                l.append(True)
            else:
                l.append(False)
            
        for k in range(len(l)-1):
            if l[k] == l[k+1]:
                flag = False
                break
            else: 
                flag = True
        
        if flag:
            print(j)
            break
    else:
        print('0')