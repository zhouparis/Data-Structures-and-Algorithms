def amount(A, S):
    """Given a collection of amount A of values with target sum S, find all unique combinations in which A values
    amounts up to S. The program returns the combinations in a list."""
    A.sort()
    result = []
    backtrack([], S, 0, A, result)

    return result

def backtrack(temp, target, start, A, result):
    """Backtracking function used to solve the amount wrapper function."""

    # Target is reached, add to results
    if target == 0 and temp not in result:
        result.append(temp)
        return

    # Target not reached, continue backtracking
    for index in range(start, len(A)):

        # If current value is greater than target, break
        if A[index] > target:
            break

        # Add current value to temporary combination and continue backtracking.
        backtrack(temp + [A[index]], target - A[index], index + 1, A, result)