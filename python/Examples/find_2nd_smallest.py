def find_2nd_smallest(list1):
    largest = list1[0]
    lowest =  list1[0]
    largest2 = None
    lowest2 = None
    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or item > largest2:
             largest2 = item
        elif item < lowest:
             lowest2 = lowest
             lowest  = item
        elif lowest2 == None or item < lowest2:
             lowest2 = item

    print(largest, largest2, lowest , lowest2)
#print(find_2nd_smallest([1,2,3,4,5]))