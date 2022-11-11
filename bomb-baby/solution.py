# But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.

# For example, if you had 3 Mach bombs and 2 Facula bombs,
# they could either PRODUCE
# 3 Mach bombs and 5 Facula bombs, or
# 5 Mach bombs and 2 Facula bombs. 
# The replication process can be changed each cycle.

# NOTE: Man starter med 1 mach bombe og 1 fach bombe

# TODO: finde ud af hvor mange layers jeg skal generate ca
# TODO: make check in layer creation: 
# check if the x,y or y,x exists in layer; = is in layer currently created
# if x,y or y,x is less than all in next layer; = is not possible
def solution(x, y):
    root = [[(1,1)]]
    curr_l = sum(root[0][0])
    int_x = int(x)
    int_y = int(y)
    depth = int_x
    if int_y > int_x:
        depth = int_y
    for each in range(depth):
        root.append(create_layer(root))
        root.remove(root[0])
        # print(root)
        if (int_x,int_y) in root[-1] or (int_y,int_x) in root[-1]:
            return(str(each+1))
        # for e in root[-1]:
        #     if sum(e) > curr_l:
        #         curr_l = sum(e)
        # if curr_l > int_x + int_y:
    return "impossible"
            # if e > (int_x,int_y) < e or (int_y,int_x) < e:
            #     return "impossible"
    # in_tree = check_in_tree(root, int_x, int_y)
    # if not in_tree:
    #     return "impossible"
    # else:
    #     return str(in_tree)

def check_in_tree(root, x,y):
    check = (x,y)
    check_flipped = (y,x)
    i = 0
    for layer in root:
        i-=-1
        if check in layer or check_flipped in layer:
            return i
    return False

def create_layer(root):
    # 1 mach cycle
    # 1 facu cycle
    layer = root[-1]
    len_layer = len(layer)
    temp = []
    # s = 0
    for i in range(len_layer):
        # facula bomb creation - Mach cycle
        temp.append(M_cycle(layer[i]))
        # mach bomb creation Facule cycle
        temp.append(F_cycle(layer[i]))
    # for each in temp:
    #     s = s + sum(each)
    # print(s)
    # print(layer)
    return temp

def M_cycle(b_in):
    m_in = b_in[0]
    f_in = b_in[1]
    f_out = m_in + f_in
    return m_in,f_out

def F_cycle(b_in):
    m_in = b_in[0]
    f_in = b_in[1]
    m_out = f_in + m_in
    return m_out, f_in


r0 = [(1,1)]
d1 = [[(1,1)],[(1,2),(2,1)]]
d2 = [[(1,1)],[(1,2),(2,1)],[(1,3),(3,2),(2,3),(3,1)]]



if __name__ == '__main__':
    print(solution('4', '7')) # 4
    # 0 M=1 F=1
    # 1 1 2 M_cycle creates 1 F
    # 2 1 3 M_cycle creates 1 F
    # 3 4 3 F_cycle creates 3 M
    # 4 4 7 M_cycle creates 4 F
    print(solution('2', '1')) # 1
    # 0 M=1 F=1
    # 1 2 1 F_cycle creates 1 M 
    print(solution('7','19'))
    print(solution('6','9'))
    print(solution('90','100'))
    # print(solution('98431','8730912'))