# This solution passed the 2022 the-cake-is-not-a-lie google foobar

def solution(s):
    ls = len(s)
    for i in range(ls):
        sm = s[:i+1:]
        n = s.replace(sm, '')
        if len(n) == 0:
            print(sm)
            return s.count(sm)
        

if __name__ == '__main__':
    print('abcabcabcabc = 4', solution("abcabcabcabc"))

    print('abccbaabccba = 2', solution("abccbaabccba"))