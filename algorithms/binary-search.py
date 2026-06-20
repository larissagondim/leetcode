# BINARY SEARCH ALGORITHM
## @brief algorithm that searchs for a determinate value with O(n) complexity
## @param arr: array in which the search is going to be made
## @param target: value which we're looking for
## @return: the index (if found) or -1 (if not found)

def binary_search(arr, target):
    # makes two variables to iterate from left & right 
    left, right = 0, len(arr)-1
    # they both meet in the middle
    while left <= right:
        # gets middle therm
        mid = left + (right - left) // 2
        # found target
        if arr[mid] == target:
            return mid
        # target is smaller than the middle one so left goes one position ahead
        elif arr[mid] < target:
            left = mid+1
        # target is bigger than the middle one so right goes one position back
        else:
            right = mid - 1
    # target not in arr
    return -1