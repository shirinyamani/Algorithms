#Linear Search
def linear(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

#Binary Search 
def binary(arr, left, right , val):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == val:
            return mid
        
        elif arr[mid] > val:
            return binary(arr, left, mid-1, val)

        else:
            return binary(arr,mid+1, right, val)

    return -1

    




if __name__ == "__main__":
    arr = [1,-2,3,774,5]
    print(binary(arr, 0, len(arr)-1, 5))