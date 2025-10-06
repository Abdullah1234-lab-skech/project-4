def palind(r): 
    e=len(r) - 1
    s = 0 
    while(s < e):
        if r[s] != r[e]:
            return False
        s += 1
        e -=1
    return True 
r = (15,62,37,37,62,15)     
if palind(r): 
    print('the tuple is flip - flop') 
else:
    print('the tuple is not flip - flop') 