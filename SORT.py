
#升序排列
def INSERTION_SORT_UP(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

#降序排列
def INSERTION_SORT_DOWN(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]<key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

#分治法
def MERGE(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0,n1):
        L.append(A[p+i])
    for j in range(0,n2):
        R.append(A[q+j+1])
    L.append(100000)
    R.append(100000)

    i = 0
    j = 0
    print(L,R)
    for k in range(p,r+1):
        if L[i]<= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


#归并排序算法
def MERGE_SORT(A,p,r):
    if p<r:
        q = (p+r)//2
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
        MERGE(A,p,q,r)


A = [4,5,6,7,1,2,3,9]
B = [4,5,6,7,1,2,3]
# INSERTION_SORT_UP(A)
print(A)
MERGE_SORT(A,0,7)
print(A)


#数组的划分
def PARTITOPN(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp

    return (i+1)

#快速排序算法
def QUICKSORT(A,p,r):
    if p<r:
        q = PARTITOPN(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

A = [2,8,7,1,3,5,6,4]
QUICKSORT(A,0,7)
print(A)

#快速排序的随机化版本
import numpy as np

def RANDOMIZED_PARTITION(A,p,r):
    i = np.random.randint(p,r+1,1).item()
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return (PARTITOPN(A,p,r))

def RANDOMIZED_QUICKSORT(A,p,r):
    if p<r:
        q = RANDOMIZED_PARTITION(A,p,r)
        RANDOMIZED_QUICKSORT(A,p,q-1)
        RANDOMIZED_QUICKSORT(A,q+1,r)

A = [2,8,7,1,3,5,6,4,10,11,19,20,51,12,13,14]
RANDOMIZED_QUICKSORT(A,0,len(A)-1)
print(A)

# #计数排序
# def COUNTING_SORT(A,B,k):
#     C = np.zeros(k)
#
#     for j in range(0,len(A)):
#         t = int(A[j])
#         print(t)
#         C[t] = C[t] + 1
#         print(C)
#         # C[i] 此时包含了A中元素的个数
#         for i in range(1,k):
#             C[i] = C[i] + C[i-1]
#         for j in range(int(len(A)-1),0,-1):
#             # B[int(C[int(A[j])])] = A[j]
#             t = A[j]
#
#
#             B[1] = 1
#             C[int(A[j])] = C[int(A[j])] - 1
#
# A = [2,5,3,0,2,3,0,3]
# B = np.zeros(len(A))
# k = 6
# COUNTING_SORT(A,B,k)
# print(B)
