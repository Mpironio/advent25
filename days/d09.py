

def s1():
    m = []
    with open('./inputs/d09.txt') as f:
        while l:= f.readline():
            m.append(l.strip().split(','))
    mlocal = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if j == i:
                continue
            c1,f1 = int(m[i][0]), int(m[i][-1])
            c2,f2 = int(m[j][0]), int(m[j][-1])
            
            area = (abs(c2 - c1) + 1) * (abs(f2 - f1) + 1)
            if area > mlocal:
                mlocal = area

    return mlocal

def s2():
    m = []
    with open('./inputs/d09_test.txt') as f:
        while l:= f.readline():
            m.append(list(map(int, (l.strip().split(',')))))
    print(m)

    ms = sorted(m, key=lambda e: (e[1], e[0]))
    print(ms)

    squares = []
    temp = []
    for i in range(len(ms) - 1):
        if ms[i][1] == ms[i+1][1]:
            temp.append(ms[i])
        else:
            temp.append(ms[i])
            squares.append(temp)
            temp = []
    print(squares)

s1()
s2()
