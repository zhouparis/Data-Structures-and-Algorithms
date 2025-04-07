# Paris Zhou

def max_independent_set(nums):
    """Function that finds the non consecutive set in a set of numbers that makes up the maximum sum"""
    # Edge case handling, array of size 1 and empty array

    if not nums:
        return []

    length = len(nums)

    if length <= 1:
        if nums[0] <= 0:
            return []
        return nums

    # Array for sums, will follow our subsequence array to record max sums
    sum_subarray = [0 for _ in range(length)]

    # Array for tracking sums of subsequences for the optimal sub array
    ssArray = [[] for _ in range(length)]

    # Initialize the first element of our first sub-sequence
    sum_subarray[0] = nums[0]
    ssArray[0] = [nums[0]]

    # Initialize the second element of our first sub-sequence
    sum_subarray[1] = max(nums[0],nums[1])
    ssArray[1] = [max(nums[0],nums[1])]

    # Fill the dynamic programming array
    for index in range(2, length):
        current_sum = nums[index] + sum_subarray[index-2]
        sum_subarray[index] = max(current_sum, sum_subarray[index - 1])

        # Determine if the current sum is greater or if the previous sum is greater
        if current_sum > sum_subarray[index-1]:
            ssArray[index] = ssArray[index-2] + [nums[index]]
        else:
            ssArray[index] = ssArray[index-1]

    # Return the largest sum possible, if it is equal to or less than 0 return an empty array.
    if sum_subarray[-1] <= 0:
        return []
    else:

        # Our algorithm handles not including negatives in sums but if the base cases are negative then we have to
        # remove the first element from the set
        if ssArray[-1][0] <= 0:
            return ssArray[-1][1:]
        return ssArray[-1]

