import time

def open_input(day, test=False):
    m = []
    path = f"inputs/d{day}"
    if test: path + "_test"
    with open(path + ".txt") as f:
        while l:= f.readline():
            m.append(list(l.strip()))
    return m


def check_around(m, x, y):
    count = 0
    for i in range(-1, 2):
        if x + i < 0: continue
        if x + i > len(m) - 1: continue
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if y + j < 0: continue 
            if y + j > len(m) - 1: continue
            
            c = m[x+i][y+j]
            if c == '@':
                count+=1
    return count

def check(m):
    rolls = []
    count = 0
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            c = m[i][j]
            if c == '.' : continue
            if check_around(m, i, j) < 4:
                count+=1
                rolls.append((i, j))
    for (i, j) in rolls:
        m[i][j] = '.'
    return count


def s1():
    m = open_input("04", False)
    return check(m)

def s2():
    m = open_input("04", False)
    count = 0

    while True:
        updated = check(m)
        if updated == 0:
            break
        count+= updated
    return count

start = time.perf_counter()
print(s1())
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print(s2())
end = time.perf_counter()
print(end - start)
