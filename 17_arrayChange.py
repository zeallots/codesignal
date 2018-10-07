def arrayChange(inputArray):

    """ You are given an array of integers. On each move you are allowed to 
    increase exactly one of its element by one. Find the minimal number of moves 
    required to obtain a strictly increasing sequence from the input. """

    total_count = 0
    value_difference = 0
    for i in range(len(inputArray) -1):
        if inputArray[i+1] > inputArray[i]:
            continue
        else:
            value_difference = abs(inputArray[i+1] - inputArray[i])
            inputArray[i+1] = inputArray[i+1] + value_difference + 1
            total_count += value_difference + 1

    return total_count

