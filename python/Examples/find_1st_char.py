def find_1stnonchar(s):
    orders = []
    counts = {}
    for x in s:
        if x in counts:
            counts[x]=counts[x]+1
            #print('2nd',x)
            #print(counts,'counts')
        else:
            counts[x]=1
            orders.append(x)
            #print('1st',x)
            #print('counts','counts')
    print(orders,'orders')
    i = 0
    for x in orders:
        if counts[x] == 1:
            i+=1
        if i ==2:
            return x
            print('x',x)


##print(find_1stnonchar('abcabcde'))