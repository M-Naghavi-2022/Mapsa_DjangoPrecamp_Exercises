t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    while a:
        if min(a) <= k:
            k += b[a.index(min(a))]
            b.pop(a.index(min(a)))
            a.remove(min(a))
        else:
            break
    
    print(k)