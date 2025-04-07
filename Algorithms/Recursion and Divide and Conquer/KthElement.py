# Paris Zhou
# Divide and Conquer

def kthElement(arr1, arr2, k):

    if len(arr1) == 0:
        return arr2[k - 1]

    if len(arr2) == 0:
        return arr1[k - 1]

    mid1 = len(arr1) // 2
    mid2 = len(arr2) // 2

    if arr1[mid1] <= arr2[mid2]:
        if k <= mid1 + mid2 + 1:
            return kthElement(arr1, arr2[:mid2], k)
        else:
            return kthElement(arr1[mid1 + 1:], arr2, k - mid1 - 1)
    else:
        if k <= mid1 + mid2 + 1:
            return kthElement(arr1[:mid1], arr2, k)
        else:
            return kthElement(arr1, arr2[mid2 + 1:], k - mid2 + 1)

# Example usage
Arr1 = [1, 2, 3, 5, 6]
Arr2 = [3, 4, 5, 6, 7]
k = 5
print("The {}-th element is: {}", kthElement(Arr1, Arr2, k))
