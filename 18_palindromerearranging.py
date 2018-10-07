def palindromeRearranging(inputString):
    """ Given a string, find out if its characters can be rearranged 
    to form a palindrome. """
    character_count = {}
    
    for c in inputString:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    
    odd_occ = [l for l in character_count if character_count[l] % 2 != 0]
    if len(odd_occ) > 1:
        return False
    else:
        return True




    
