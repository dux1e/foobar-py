# But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.

# For example, if you had 3 Mach bombs and 2 Facula bombs,
# they could either PRODUCE
# 3 Mach bombs and 5 Facula bombs, or
# 5 Mach bombs and 2 Facula bombs. 
# The replication process can be changed each cycle.

# NOTE: Man starter med 1 mach bombe og 1 fach bombe

def solution(x, y):
    M = 1; F = 1
    cycles = x
    if x > y:
        cycles = x
    for c in range(cycles):
        if x == M and y == F:
            return "0"
        
        pass
    else:
        return "impossible"

def M_cycle(m):
    m_in = m
    m_out = 0
    for M in range(m_in)
        m_out-=-1
    return m_out

def F_cycle(f):
    return f

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
