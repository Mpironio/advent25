import time
def open_input(day, test=False):
    m= []
    path = f"inputs/d{day}"
    if test: path+= "_test"
    with open(path + ".txt") as f:
        while l:= f.readline():
            m = l.strip()
    return m
m = open_input("02", False)
def s1():
    mc = m.split(',')
    total = 0
    for r in mc:
        l, u = map(int, r.split('-'))
        for i in range(l, u+1):
           total+=check(str(i)) 
    
    return total

def s2():
    mc = m.split(',')
    total = 0
    return total

def check(s):
    if len(s) == 2 and s[0] == s[1] and s[0] != '0':
        return int(s)
    elif len(s) == 2 and s[0] != s[1]:
        return 0
    elif len(s) % 2 == 1: return 0
    elif s.startswith('0'): return 0
    l = len(s) // 2
    if len(s) % 2 == 0:

        if s[l:] == s[:l]: 
            return int(s)
        c1 = check(s[l:])
        c2 = check(s[:l])
        if c1 == c2:
            return int(c1 + c2)
    return 0


start = time.perf_counter()
print(s1())
end = time.perf_counter()
print(end - start)
start = time.perf_counter()
print(s2())
end = time.perf_counter()
print(end - start)
