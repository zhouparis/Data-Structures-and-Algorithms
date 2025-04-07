# Top down approach for dna matching
# Paris Zhou

def dna_match_topdown(DNA1, DNA2):
    # Dictionary initialized to memorize results
    memoize = dict()
    return recursive_helper(DNA1,DNA2, len(DNA1), len(DNA2), memoize)

def recursive_helper(DNA1, DNA2, index1, index2, memoize):
    # Return the result if it's already computed
    if (index1, index2) in memoize:
        return memoize[(index1, index2)]

    # Base case: if any string is empty
    if index1 == 0 or index2 == 0:
        memoize[(index1, index2)] = 0

    # if the DNA base pairs match
    elif DNA1[index1-1] == DNA2[index2-1]:
        memoize[(index1,index2)] = 1 + recursive_helper(DNA1, DNA2, index1 -1, index2 - 1, memoize)

    # if the DNA base pairs do not match
    else:
        memoize[(index1, index2)] = max(recursive_helper(DNA1,DNA2, index1, index2-1,memoize), recursive_helper(DNA1,DNA2,index1-1, index2, memoize))
    return memoize[(index1,index2)]

# Bottom up approach for dna matching
# Paris Zhou

def dna_match_bottomup(DNA1,DNA2):
    dna1_length, dna2_length = len(DNA1), len(DNA2)

    # Initialize table with all zeros
    dynamic_table = [[0]*(dna2_length+1) for _ in range (dna1_length+1)]

    for index1 in range (1, dna1_length+1):
        for index2 in range (1, dna2_length+1):
            if DNA1[index1-1] == DNA2[index2-1]:
                dynamic_table[index1][index2] = dynamic_table[index1-1][index2-1] +1
            else:
                dynamic_table[index1][index2] = max(dynamic_table[index1 - 1][index2], dynamic_table[index1][index2-1])

    return dynamic_table[dna1_length][dna2_length]