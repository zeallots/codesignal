def areSimilar(a, b):
    """  Two arrays are called similar if one can be obtained from 
    another by swapping at most one pair of elements in one of the arrays.
    Given two arrays a and b, check whether they are similar.
    """
    count = 0
    list_a = []
    list_b = []
    for i in range(len(a)):
        if (a[i]!= b[i]):
            count +=1
            list_a.append(a[i])
            list_b.append(b[i])

    if (count ==0):
        return True 

    elif count ==2: 
        return sorted(list_a)==sorted(list_b)

    else:
        return False
