def open_input(day, test=False):
    m = []
    path = f"inputs/d{day}"
    if test: 
        path += "_test"
    with open(path + ".txt") as f:
        while l:= f.readline():
            m.append(l.strip())
    return m

def s1():
    m = open_input("05", False)
    sep, _ = [(i, r) for i, r in enumerate(m) if r == ''].pop()
    
    rss = m[:sep]
    vs = list(map(int, m[sep+1:]))

    rs = []
    for r in rss:
        b = list(map(int, r.split('-')))
        rs.append(b)

    done = set()
    for [lb, ub] in rs:
        for v in vs:
            if lb <= v and v <= ub:
                done.add(v)
    return len(done)

def s2():
    m = open_input("05", False)
    sep, _ = [(i, r) for i, r in enumerate(m) if r == ''].pop()
    
    rss = m[:sep]
    vs = list(map(int, m[sep+1:]))

    rs = []
    for r in rss:
        b = list(map(int, r.split('-')))
        rs.append(b)
    
    rs = sorted(rs, key=lambda l: l[0])
    print(*rs, sep='\n')
    
    i = 0
    while i < len(rs) - 1:
        [lb, ub] = rs[i]
        [nlb, nub] = rs[i+1]
        if ub >= nlb:
            rs[i]=[lb, max(ub, nub)]
            rs.pop(i+1)
        else:
            i+=1
    total = sum(map((lambda r: r[1] - r[0] + 1), rs))
    return total


print(s1())
print(s2())