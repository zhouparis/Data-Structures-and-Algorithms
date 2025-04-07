# Paris Zhou

def powerset(input_set):
    """Wrapper function that calls the backtracking function"""
    # Create answer set that will be used by the backtracking algorithm to store calculated sets
    answer = []
    backtrack(input_set, [], answer)
    return answer


def backtrack(input_set, current_set, answer):
    """Function that finds the powerset of an inputted set provided by the wrapper function powerset().
    It uses backtracking to find all sets within an initial set provided. It makes many redundant calls and
    brute forces finding all combinations."""
    answer.append(current_set[::])

    for index in range(len(input_set)):
        current_set.append(input_set[index])
        backtrack(input_set[index + 1:], current_set, answer)

        # Pop returns values and unravels the recursive calls
        current_set.pop()
