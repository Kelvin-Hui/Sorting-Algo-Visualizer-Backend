import random

def randomArray(n : int) -> list:
    return random.sample(range(1,600),n)

def animatedArray(algo : str , arr : list) -> list:
    algo_options = {
    "selectionSort" : selectionSort ,
    "insertionSort" : insertionSort ,
    "bubbleSort"   : bubbleSort ,
    "mergeSort"     : mergeSort ,
    "heapSort"      : heapSort ,
    "quickSort"     : quickSort
    }
    return ([i.copy() for i in algo_options[algo](arr)])

def algocomplexity(algo : str) -> dict:
    algo_complexity = {
        "selectionSort" : {
            "Best" : "O(n^2)",
            "Average" : "O(n^2)",
            "Worst" : "O(n^2)"
        } ,
        "insertionSort" : {
            "Best" : "O(n)",
            "Average" : "O(n^2)",
            "Worst" : "O(n^2)"
        } ,
        "bubbleSort"   : {
            "Best" : "O(n^2)",
            "Average" : "O(n^2)",
            "Worst" : "O(n^2)"
        } ,
        "mergeSort"     : {
            "Best" : "O(n log(n))",
            "Average" : "O(n log(n))",
            "Worst" : "O(n log(n))"
        } ,
        "heapSort"      : {
            "Best" : "O(n log(n))",
            "Average" : "O(n log(n))",
            "Worst" : "O(n log(n))"
        } ,
        "quickSort"     : {
            "Best" : "O(n log(n))",
            "Average" : "O(n log(n))",
            "Worst" : "O(n^2)"
        }
    }
    return (algo_complexity[algo])



def selectionSort(arr : list) -> list :
    yield arr
    #Going through the list
    for i in range(len(arr)):
        min_index = i
        #Going throught the rest of the list to find the smallest element
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            yield arr
        #Swap
        arr[i],arr[min_index] = arr[min_index],arr[i]
        yield arr

def insertionSort(arr : list) -> list:
    yield arr
    for i in range(1,len(arr)):
        cur = arr[i]
        
        j = i
        while j > 0  and cur < arr[j-1]:
            #Swap
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
            yield arr
    yield arr

def bubbleSort(arr : list) -> list:
    yield arr
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                #Swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
                yield arr

def mergeSort(arr : list , low_ind = 0 , high_ind = None) -> list:
    if high_ind == None:
        high_ind = len(arr)-1
        
    if len(arr) <= 1:
        return arr
    if low_ind >= high_ind:
        return 
        
    mid = (low_ind + high_ind) //2
    
    yield from mergeSort(arr,low_ind,mid)
    yield from mergeSort(arr,mid+1,high_ind)
    yield from mergeSortHelper(arr,low_ind,mid,high_ind)
    yield arr

def mergeSortHelper(arr : list , low , mid , high) -> list:
    i = low
    j = mid+1
    temp = []
    
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
            
    if(i>mid):
        while(j<=low):
            temp.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            temp.append(arr[i])
            i+=1

    for index,value in enumerate(temp):
        arr[low+index] = value
        yield arr

def heapSort(arr : list) -> list:
    yield arr
    for i in range(len(arr)//2 - 1 , -1 ,-1):
        yield from heapify(arr,len(arr),i)
    
    for j in range(len(arr)-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        yield arr
        yield from heapify(arr,j,0)

def heapify(arr : list,n : int,i : int):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
    
        yield from heapify(arr,n,largest)
        yield arr

def quickSort(arr : list, low = 0  , high  = None) -> list:
    if high == None:
        high = len(arr)-1
    if low < high:
        yield arr
        i = low 
        pivot = arr[high]
        
        for j in range(low,high):
            if arr[j] < pivot:
                arr[i],arr[j] = arr[j], arr[i]
                i+=1
                yield arr
        
        arr[i],arr[high] = arr[high],arr[i]
        yield arr
        
        yield from quickSort(arr,low,i-1)
        yield from quickSort(arr,i+1,high)