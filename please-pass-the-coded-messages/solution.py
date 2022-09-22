# This solution passed the 2022 please-pass-the-coded-messages google foobar
# Level 2 Test 1

import itertools
def solution(l):
    temp = []
    largest = 0
    for L in range(len(l) + 1):
        for subset in itertools.combinations(l, L):
            for eachperm in itertools.permutations(subset):
                try:
                    temp.append(int(''.join(str(i) for i in eachperm)))
                except:
                    continue
    s = sorted(temp, reverse=True)
    for each in s:
        if each % 3 == 0 and each > largest:
            largest = each
    return largest


def test():
    l = [3, 1, 4, 1]
    for L in range(len(l) + 1):
        for subset in itertools.combinations(l, L):
            print(subset)

    array = itertools.permutations(l)
    temp = []
    for eachpermutation in array:
        temp.append(int(''.join(str(i) for i in eachpermutation)))
    s = sorted(temp, reverse=True)
    for each in s:
        print(each)


def test2():
    l = [3, 1, 4, 1]
    temp = []
    largest = 0
    for L in range(len(l) + 1):
        for subset in itertools.combinations(l, L):
            for eachperm in itertools.permutations(subset):
                try:
                    temp.append(int(''.join(str(i) for i in eachperm)))
                except:
                    continue
    s = sorted(temp, reverse=True)
    for each in s:
        if each % 3 == 0 and each > largest:
            largest = each
    return largest


if __name__ == '__main__':
    # l = [3, 1, 4, 1]
    # print(list(itertools.permutations(l)))
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))



# https://stackoverflow.com/questions/43630183/running-through-combinations-of-4-numbers
# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
