# s1051526 Algorithm_HW2
# find kth biggest element from a unordered list in linear time
import random
import math
def select(A,k):
    if len(A)<=5:
        return sorted(A)[k]
    subs=[A[x:x+5] for x in range(0,len(A),5)] # slice A every 5 elements
    meds=[select(sub,math.floor((len(sub)-1)/2)) for sub in subs] # find meds in every subset
    med=select(meds,math.floor((len(meds)-1)/2)) # find med of meds
    small=[x for x in A if x <med]
    equal=[x for x in A if x==med]
    big  =[x for x in A if x >med]
    if k<len(small)               :return select(small,k)
    elif k<(len(equal)+len(small)):return med
    else                          :return select(big,k+len(big))
 
A=[random.randint(0,500) for x in range(100)]
print(A)
print(sorted(A)[math.floor(len(A)/2)])
print(select(A,math.floor(len(A)/2)))
finish=input()