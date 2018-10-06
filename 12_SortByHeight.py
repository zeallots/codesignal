""" Some people are standing in a row in a park. There are trees between 
them which cannot be moved. Your task is to rearrange the people by their 
heights in a non-descending order without moving the trees. 
People can be very tall! """

def sortByHeight(a):
    people_list = sorted([i for i in a if i != -1])
    tree_position_list = [x for x in range(len(a)) if a[x] == -1]
    for tree in tree_position_list:
        people_list.insert(tree, -1)
    return people_list

