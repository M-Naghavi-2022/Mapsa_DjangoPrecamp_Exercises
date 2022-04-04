r = int(input())
for i in range(r):
    n = int(input())
    a = list(map(int, input().split()))
    for j in a:
        l = []
        for k in a:
            if k%j == 0:
                l.append(0)
            else:
                l.append(1)
            
        for k in range(n-1):
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