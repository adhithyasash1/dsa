L = [7, 9, 11, 33, 99, 233, 343, 434, 445, 454, 545, 999, 2, 2, 4, 5, 5]
M = [7, 8, 2, 4, 5, 6]

def findMax(arr, low, high):
 
    # If there is only one element left
    if (high == low):
        return arr[low]
 
    # Find mid
    mid = low + (high - low) // 2
    # Check if mid reaches 0 ,it is greater than next element or not
    if(mid==0 and arr[mid]>arr[mid+1]):
          return arr[mid]
 
    # Check if mid itself is maximum element
    if (mid < high and arr[mid + 1] < arr[mid] and mid>0 and arr[mid]>arr[mid-1]):
        return arr[mid]
     
    # Decide whether we need to go to
    # the left half or the right half
    if (arr[low] > arr[mid]):
        return findMax(arr, low, mid - 1)
    else:
        return findMax(arr, mid + 1, high)
 
# Driver code
def findLargest(L):
    n = len(L)
    print(findMax(L, 0, n - 1))
