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
    ms = 1
    fs = 1
    pass

def mach_cycle(x, y):
    pass

def facu_cycle(x, y):
    pass

if __name__ == '__main__':
    print(solution('4', '7')) # 4
    # 1 
    # 2 
    # 3 
    # 4 
    print(solution('2', '1')) # 1
    # 1 facu_cycle creates 1 mach bomb = 2 mach 1 facu 
