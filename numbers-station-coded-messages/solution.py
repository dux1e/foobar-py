# This solution passed the 2022 numbers-station-coded-messages google foobar
# Level 2 Test 2  

def solution(l,t):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if sum(l[i:j+1:]) == t:
                return i,j
    return -1,-1

def maybe():
    l = [4, 3, 5, 7, 8]
    t = 15
    print(l[0:])
    n = len(l)
    for i in range(n):
        for j in range(n):
            if sum(l[i:j+1:]) == t:
                return i,j
    return -1,-1

def tried(l,t): # passed test 1 - 4 failed hidden 5
    n = len(l)
    E = int((n*(n+1)/2))
    i = 0
    j = 1
    p = 1
    for q in range(E):
        # print(sum(l[i:j:]))
        # print('i',i,'j',j,l[i:j:])
        if sum(l[i:j:]) == t:
            # if i == j:
                # print('Not')
            # print('i',i,'j',j)
            # print(l[i:j:])
            # print(sum(l[i:j:]))
            # print( i,j-1 )
            if i != j-1:
                print( i,j-1 )
                return i,j-1
        # print(l[i:j:])
        i = i + 1
        j = j + 1
        if j == n + 1:
            i = 0
            j = p + 1
            p = p + 1
        if p == n + 1:
            return -1,-1
    

if __name__ == '__main__':
    print(solution([1, 2, 3, 4], 15)) # -1,-1
    print(solution([4, 3, 10, 2, 8], 12)) # 2,3
    print(solution([1,2,3,4],3)) # 2,2 curr
    print(solution([1],3)) # -1,-1
    print(maybe())
    # These currently return
    # (-1, -1)
    # (2, 3)
    # (2, 2)
    # (-1, -1)
    # l = [1,2,3,4]
    # n = len(l)
    # tri = int((n*(n+1)/2))

    # print(sum([3,10]))
    
    # print(test([1,2,3,4], 5))
    # 1st loop iter
    # print(l[0:1:])
    # print(l[1:2:])
    # # 2nd loop iter
    # print(l[0:2:])
    # print(l[1:3:], 'sum', sum(l[1:3:]))
    # # last loop iter
    # print(l[0:len(l):])
    # n = len(l)
    # tri = int((n*(n+1)/2))
    # print(tri)

    # for every_sublist in list:
        # if sum(current_sublist) == t
            # get_startindex_of_sublist, get_endindex_of_sublist compared to input list
            # https://stackoverflow.com/questions/17870544/find-starting-and-ending-indices-of-sublist-in-list
        # else
            #-1,-1

    # For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, 
    # the function solution(l, t) would return the list [0, 2] 
    # because the list l contains the sub-list [4, 3, 5]
    # Check list this way
    # for l = [4, 3, 5, 7, 8]
    # loops iteration for l are sigma_sum(len(l)) = (n*(n+1)/2) where n is the length l
    # [4]
    # [4,3]
    # [4,3,5]
    # [4,3,5,7]
    # [4,3,5,7,8]
    # [3]
    # [3,5]
    # [3,5,7]
    # [3,5,7,8]
    # [5]
    # [5,7]
    # [5,7,8]
    # [7]
    # [7,8]
    # [8]
    