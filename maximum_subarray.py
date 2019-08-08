#By:shenqiti


def FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high):
    left_sum = -10000
    sum = 0
    for i in range(low,mid+1):
        sum = sum + A[i]
        if sum >left_sum:
            left_sum = sum
            max_left = i
    right_sum = -10000
    sum = 0
    for j in range(mid+1,high+1):
        sum = sum + A[j]
        if sum >right_sum:
            right_sum = sum
            max_right = j
    print(max_left,max_right,left_sum+right_sum)
    return (max_left,max_right,left_sum+right_sum)

#设计求解最大子数组问题的分治算法
def FIND_MAXIMUM_SUBARRAY(A,low,high):
    if high == low:
        return (low,high,A[low])    #只有一个元素
    else:
        mid = (low+high)//2
        left_low,left_high,left_sum = FIND_MAXIMUM_SUBARRAY(A,low,mid)
        right_low,right_high,right_sum = FIND_MAXIMUM_SUBARRAY(A,mid+1,high)
        cross_low,cross_high,cross_sum = FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high)

        if left_sum>= right_sum and left_sum>=cross_sum:
            print(left_low,left_high,left_sum)
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum >=cross_sum:
            print(right_low,right_high,right_sum)
            return (right_low,right_high,right_sum)
        else:
            print(cross_low,cross_high,cross_sum)
            return (cross_low,cross_high,cross_sum)
A = [2,9,3,4,-4,5]
FIND_MAX_CROSSING_SUBARRAY(A,1,3,5)
FIND_MAXIMUM_SUBARRAY(A,0,5)


