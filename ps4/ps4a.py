#!/usr/bin/env python3
# Problem Set 4A
# Name: John L. Jones
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    
    if len(sequence) <= 1:
        permutations.append(sequence)
    
    else:
        sub_perms = get_permutations(sequence[1:])
        for s in sub_perms:
            for i in range(len(s)+1):
                permutations.append(s[:i] + sequence[0] + s[i:])

    return permutations

if __name__ == '__main__':
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:  ', get_permutations(example_input))
    
    example_input = 'ab'
    print('')
    print('Input:', example_input)
    expected_output = ['ab', 'ba']
    expected_output.sort()
    actual_output = get_permutations(example_input)
    actual_output.sort()
    print('Expected Output:', expected_output)
    print('Actual Output:  ', actual_output) 

    example_input = 'abc'
    print('')
    print('Input:', example_input)
    expected_output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    expected_output.sort()
    actual_output = get_permutations(example_input)
    actual_output.sort()
    print('Expected Output:', expected_output)
    print('Actual Output:  ', actual_output)

    example_input = 'cat'
    print('')
    print('Input:', example_input)
    expected_output = ['cat', 'act', 'atc', 'tca', 'cta', 'tac']
    expected_output.sort()
    actual_output = get_permutations(example_input)
    actual_output.sort()
    print('Expected Output:', expected_output)
    print('Actual Output:  ', actual_output)

    example_input = 'zyx'
    print('')
    print('Input:', example_input)
    expected_output = ['zyx', 'zxy', 'yzx', 'yxz', 'xyz', 'xzy']
    expected_output.sort()
    actual_output = get_permutations(example_input)
    actual_output.sort()
    print('Expected Output:', expected_output)
    print('Actual Output:  ', actual_output)
