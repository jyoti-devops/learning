def find2nd_largest(list1):
    lg = list1[0]
    lg2 = list1[0]
    for item in list1[1:]:
        if item > lg:
            lg = item
    for item in list1[1:]:
        if item != lg and item > lg2:
            lg2 = item

    print('largest-{},largest2-{}'.format(lg,lg2))
    print(find2nd_largest([-1,-2,-3,-4.5,6.0]))