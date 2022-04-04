def req_att(h,d):                       # calculates required attacks to defeat the competitor
    if h%d == 0:
        return h//d
    else:
        return (h//d) + 1

def char_win(hc, dc, hm, dm):           # checks if the character can win by the given parameters
    w_c = req_att(hm,dc)
    w_m = req_att(hc,dm)

    if w_c <= w_m:
        return True
    else:
        return False

r = int(input())
for i in range(r):
    h_c, d_c = map(int, input().split())
    h_m, d_m = map(int, input().split())
    k, w, a = map(int, input().split())

    if char_win(h_c, d_c, h_m, d_m):    # checks if the character can win by the initial condition
        print('YES')
        continue
    else:        
        for j in range(k+1):            # checks if the character can win by using k number of coins to enhance health and weapon
            h_c_tmp = h_c
            d_c_tmp = d_c
            h_c_tmp += (j * a)
            d_c_tmp += ((k-j) * w)
            if char_win(h_c_tmp, d_c_tmp, h_m, d_m):
                print('YES')
                break
        else:                           # if there is no way for the character to win
            print('NO')