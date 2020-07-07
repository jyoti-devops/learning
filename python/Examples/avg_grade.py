def avgrade(dict1):
    stu = {}
    marks={}
    avg ={}

    for i in dict1:
        #print(i.keys())
        #print('stu',stu)
        name = i.keys()[0]
        print(name,'name')
        if name in stu:
            #name = i.keys()
            print(name,'name')
            stu[name] +=1
        else:
            stu[name] = 1

        if name in marks:
            marks[name] += int(i.values()[0])
        else:
            marks[name] = int(i.values()[0])
    for j in stu:
        print(stu[j],'stu')
        avg[j] = marks[j]/stu[j]
        print(avg[j])

    print('avg', max(avg.values()))

dict1=[{'jo':'40'}, {'jo1':'40'},{'jo2':'60'}, {'jo2':'10'}]

print (avgrade(dict1))