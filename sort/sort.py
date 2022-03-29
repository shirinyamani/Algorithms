#Bubble Sort  #Time: O(n^2) #Space O(n) cuz it happens in-place! no extra spce needed!
def bubbleSort(customlist):
    for i in range(len(customlist)-1):
        for j in range(len(customlist)-i-1): #every time we need to minimize the element that we have alrealy sort it!
            if customlist[j] > customlist[j+1]: #if next> curr --> swap
                customlist[j], customlist[j+1] = customlist[j+1], customlist[j]  
    print(customlist)

#Selection Sort#Time: O(n^2) #Space O(n) cuz it happens in-place! no extra spce needed!
def selectionSort(customlist):
    for i in range(len(customlist)): #to loop thro all elements!
        #step 1: find min
        min_index = i 
        for j in range(i+1, len(customlist)): #to compare with all elements after i!
            if customlist[min_index] > customlist[j]:
                min_index = j #update min_index
        customlist[i], customlist[min_index] = customlist[min_index], customlist[i]
    print(customlist)

#insertion Sort#Time: O(n^2) #Space O(n) cuz it happens in-place! no extra spce needed!
def insertionSort(customlist): 
    for i in range(1, len(customlist)): #loop thro all elements
        key = customlist[i] #pick the first element
        j = i - 1 
        while j>=0 and key < customlist[j]:
            customlist[j+1] = customlist[j]
            j -= 1
        customlist[j+1] = key
    print(customlist)
            
#Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        mergeSort(left) #on each half 
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i]<right[j]: #start backing up the merge
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left): #check whether any elements left!
            arr[k] = left[i]
            i +=1
            k +=1

        while j< len(right):
            arr[k] = right[j]
            j+= 1
            k+= 1
        
    print(arr)

#Quick Sort
def partition(start, end, arr): #pich the very last or first element as pivot
    #Initializing pivot's index to start
    pivot_index = start
    pivot = arr[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        # Decrement the end pointer till it finds an
        # element less than pivot
        while arr[end] > pivot:
            end -=1
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            arr[start], arr[end] = arr[end], arr[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end] 

    # Returning end pointer to divide the array into 2
    return end 

def quickSort(start, end, arr):
    if (start < end):

        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, arr)

        # Sort elements before partition
        # and after partition
        quickSort(start, p-1, arr)
        quickSort(p+1, end, arr)
    print(arr)

#Heap Sort






if __name__ == "__main__":
    arr = [1,3,5,6,-3,766,-10.5]
    print(quickSort(0, len(arr)-1, arr))

