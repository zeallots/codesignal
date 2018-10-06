
def reverse_parentheses(s):
    """ You have a string s that consists of English letters, punctuation marks, 
    whitespace characters, and brackets. 
    It is guaranteed that the parentheses in s form a regular bracket sequence.

    parentheses, starting from the innermost pair. The results string should 
    Your task is to reverse the strings contained in each pair of matching 
    not contain any parentheses. """
    list_char = list(s)
    open_bracket_index_pos = []
    for i, v in enumerate(list_char):
        if v == '(':
            open_bracket_index_pos.append(i)
        elif v == ')':
            j = open_bracket_index_pos.pop() #j position would be lower than i
            list_char[j:i] = list_char[i:j:-1]
    return ''.join(x for x in list_char if x not in '()')
