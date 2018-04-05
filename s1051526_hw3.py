# s1051526 Algorithm_HW3
# find Longest Common Subsequence by dynamic programming
def FindLCS(s1,s2):
    #find length of LCS
    table=[[0 for y in range(len(s2)+1)] for x in range(len(s1)+1)]
    for x in range(1,len(s1)+1):
        for y in range(1,len(s2)+1):
            if s2[y-1] is s1[x-1]:
                table[x][y]=(max(table[x-1][y],table[x][y-1],table[x-1][y-1]+1))
            else:
                table[x][y]=(max(table[x-1][y],table[x][y-1]))
    length=table[len(s1)][len(s2)]
    print('Length of LCS is : ',length)
    #find LCS
    LCS=""
    x,y=len(s1),len(s2) # find LCS from last char
    while x is not 0 and y is not 0:
        if table[x][y] is table[x-1][y]: #go left
            x-=1
        elif table[x][y] is table[x][y-1]: #go up
            y-=1
        else: # match
            LCS=s2[y-1]+LCS # or LCS=s1[x-1]+LCS
            x-=1
            y-=1
    return LCS

print(FindLCS(input(),input()))
finish=input()