# s1051526 Algorithm_HW1
# randomized quicksort
import random
def QS(arr):    # spend more space
    if len(arr)<=1: return arr
    p=arr[random.randint(0,len(arr)-1)]
    return QS([x for x in arr if x<p]) + [x for x in arr if x==p] + QS([x for x in arr if x>p])

#[print(x) for x in QS([int(input()) for size in range(0,int(input()))])]
A=[random.randint(0,500) for x in range(100)]
print(A)
print(QS(A))
finish=input()

def QS2(arr,left=0,right=0):    # in-place
    if right==0: right=len(arr)-1
    if left>=right: return arr
    pivot=random.randint(left,right)
    # take pivot to right
    arr[right],arr[pivot]=arr[pivot],arr[right] # swap(pivot,right)
    idx=left
    # throw all small than pivot to left, record by index
    for x in range(left,right):
        if arr[x]<=arr[right]:
            arr[x],arr[idx]=arr[idx],arr[x] # swap(x,idx)
            idx+=1
    # put pivot to where it should be
    arr[right],arr[idx]=arr[idx],arr[right] # swap(right,idx)
    QS2(arr,left,idx-1)
    QS2(arr,idx+1,right)
    return arr
