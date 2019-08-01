

def PARENT(i):
    return (i//2)

def LEFT(i):
    return (2*i)

def RIGHT(i):
    return (2*i+1)



#将数组转化为最大堆
def MAX_HEAPIFY(A,i):
    l = LEFT(i)
    r = RIGHT(i)
    if l<=A[0] and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<=A[0] and A[r]>A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        MAX_HEAPIFY(A,largest)

#建堆，对树中其他节点都调用一次MAX_HEAPIFY

def BUILD_MAX_HEAP(A):
    for i in range((len(A)-1)//2,0,-1):
        MAX_HEAPIFY(A,i)

#堆排序算法

def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(len(A)-1,1,-1):
        temp = A[1]
        A[1] = A[i]
        A[i] = temp
        A[0] = A[0] - 1
        MAX_HEAPIFY(A,1)


#A[0]存放堆元素的个数
A = [10,4,1,3,2,16,9,10,14,8,7]
B = [9,5,3,17,10,84,19,6,22,9]
C = [10,16,14,10,8,7,9,3,2,4,1]
BUILD_MAX_HEAP(B)
print(B)
HEAPSORT(C)
print(C)
