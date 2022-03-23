import copy
import random as rd
import numpy as np
import time
import matplotlib.pyplot as plt

#function to generate random array
def generate_fns(size):
    array=np.random.randint(0,100,size)
    return array

#insertion sort implementation
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i
        while(j>0 and arr[j-1]>key):
            arr[j]=arr[j-1]
            j=j-1
        arr[j] = key

#selection sort implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        imin=i
        for j in range(i+1,n):
            if(arr[j]<arr[imin]):
                imin=j
        if(imin!=i):
            arr[imin],arr[i]=arr[i],arr[imin]

#Quick sort implementation
def randomized_partition(array,start,end):
    pivot_index = rd.randint(start,end)
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return partition(array,start,end)

def partition(array,start,end):
    pivot = array[end]
    i = start-1
    for j in range(start,end):
        if(array[j] <= pivot):
            i +=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i+1]
    return i+1

def quick_sort(array,start,end):
    if(start < end):
        q = randomized_partition(array,start,end)
        quick_sort(array,start,q-1)
        quick_sort(array,q+1,end)


#merge sort implementation
def merge(A,start,mid,end):
    nl = mid-start+1
    nr = end-mid
    left = A[start:mid+1]
    right = A[mid+1:end+1]
    i=j=0 #i:smallest unpicked element in the left array,j:smallest unpicked element in the right array
    k=start #K: the next position to be filled in the original array
    while(i<nl and j<nr): #merging elements in order
        if(left[i] < right[j]):
            A[k] = left[i]
            i+=1
        else:
            A[k] = right[j]
            j+=1
        k+=1

    while(i<nl):
        A[k] = left[i]
        i+=1
        k+=1
    while(j<nr):
        A[k] = right[j]
        j += 1
        k += 1


def merge_sort(A,start,end): #start:first index of the array,end : last index in the array
    if(start<end):
        mid = (start+end)//2
        merge_sort(A,start,mid)
        merge_sort(A,mid+1,end)
        merge(A,start,mid,end)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sizes=[1000,25000,50000,100000]
    insertion_time=[]
    selection_time=[]
    merge_time=[]
    quick_time=[]
    for size in sizes:
        array=generate_fns(size)
        insertion_array=copy.deepcopy(array)
        selection_array=copy.deepcopy(array)
        merge_array = copy.deepcopy(array)
        quick_array = copy.deepcopy(array)

        ts=time.time()
        insertion_sort(insertion_array)
        tf=time.time()
        insertion_time.append(round(tf-ts,4))


        ts=time.time()
        selection_sort(selection_array)
        tf=time.time()
        selection_time.append(round(tf-ts,4))


        ts=time.time()
        quick_sort(quick_array,0,len(quick_array)-1)
        tf=time.time()
        quick_time.append(round(tf-ts,4))

        ts=time.time()
        merge_sort(merge_array, 0, len(merge_array) - 1)
        tf=time.time()
        merge_time.append(round(tf-ts,4))

    print('selection',selection_time)
    print('insertion', insertion_time)
    print('merge', merge_time)
    print('quick', quick_time)

    fig = plt.figure(figsize=(12, 10))
    grid = plt.GridSpec(2, 4, wspace=0.6, hspace=0.7)
    plt.subplot(grid[0, 0:])
    plt.plot(sizes, insertion_time,label = "Insertion sort")
    plt.plot(sizes, selection_time,label = "Selection sort")
    plt.plot(sizes, merge_time,label = "Merge sort")
    plt.plot(sizes, quick_time,label = "Quick sort")
    plt.xlabel('Random array sizes')
    plt.ylabel('Running time(secs)')
    plt.title('analysis of different sorting algorithms')
    plt.legend()

    plt.subplot(grid[1, 0])
    plt.plot(sizes, insertion_time)
    plt.xlabel('Random array sizes')
    plt.ylabel('Running time(secs)')
    plt.title('Insertion sort O(n^2)')

    plt.subplot(grid[1, 1])
    plt.plot(sizes, selection_time, 'tab:orange')
    plt.xlabel('Random array sizes')
    plt.ylabel('Running time(secs)')
    plt.title('Selection sort O(n^2)')

    plt.subplot(grid[1, 2])
    plt.plot(sizes, merge_time, 'g')
    plt.xlabel('Random array sizes')
    plt.ylabel('Running time(secs)')
    plt.title('Merge sort O(nlog(n))')

    plt.subplot(grid[1, 3])
    plt.plot(sizes, quick_time, 'r')
    plt.xlabel('Random array sizes')
    plt.ylabel('Running time(secs)')
    plt.title('Quick sort O(nlog(n))')

    plt.show()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
