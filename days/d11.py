
def countpaths(g, source, dst):
    res = 0
    stack = g[source]
    for e in stack:
        if e == dst:
            res+=1
        else:
            stack+=g[e]
    return res

def paths(g, src, dst, current, totalp):
    current.append(src)
    if src == dst:
        totalp.append(current.copy())
    else:
        for e in g[src]:
            paths(g, e, dst, current, totalp)
    current.pop()
    return
        




def s1():
    m = {}
    with open('./inputs/d11.txt') as f:
        while l:=f.readline():
            n, adj = l.split(':')
            adj = adj.strip().split(' ')
            m[n] = adj

    return countpaths(m, 'you', 'out')

def s2():
    m = {}
    #TEST
    # with open('./inputs/d11_test.txt') as f:
    #     f = f.read().split('PART2')[1].strip().split('\n')
    #     for l in f:
    #         print(l)
    #         n, adj = l.split(':')
    #         adj = adj.strip().split(' ')
    #         m[n] = adj
    
    with open('./inputs/d11.txt') as f:
        while l:=f.readline():
            n, adj = l.split(':')
            adj = adj.strip().split(' ')
            m[n] = adj

    totalp = []
    paths(m, 'svr', 'out', [], totalp)
    totalp = list(filter(lambda l: 'dac' in l and 'fft' in l, totalp))
    
    return len(totalp)


# print(s1())
print(s2())