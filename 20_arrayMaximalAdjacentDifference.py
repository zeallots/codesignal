def arrayMaximalAdjacentDifference(inputArray):
    """ Given an array of integers, find the maximal absolute difference 
    between any two of its adjacent elements. """    
    max_diff = 0
    for i in range(len(inputArray) - 1):
        temp_diff = abs(inputArray[i] - inputArray[i+1])
        if max_diff < temp_diff:
            max_diff = temp_diff
    return max_diff

