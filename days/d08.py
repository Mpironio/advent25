import math

def straightline(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    z = (z1 - z2) ** 2
    return (x + y + z) ** 0.5



def s1():
    m = []
    with open('./inputs/d08.txt') as f:
        while l:= f.readline():
            tmp = l.strip().split(',')
            tup = tuple(map(int, tmp))
            m.append(tup)

    pairs = [(m[i], m[j]) for i in range(len(m)) for j in range(i+1, len(m))]
    sortedPairs = sorted(pairs, key=lambda pq: straightline(pq[0], pq[1]))
    djntset = {}
    for p in m: djntset[p] = -1
    circuits = []
        
    lastBoxes = None
    for (p, q) in sortedPairs:
        pi = djntset.get(p)
        qi = djntset.get(q)

        if pi == qi and pi != -1: continue

        if pi != qi and pi != -1 and qi != -1:
            circuits[pi].extend(circuits[qi])

            for v in circuits[qi]:
                djntset[v] = pi

            last = len(circuits) - 1
            if qi != last:
                circuits[qi] = circuits[last]
                for v in circuits[qi]:
                    djntset[v] = qi
            circuits.pop()
            lastBoxes = (p, q)

        elif pi == -1 and qi == -1:
            print(pi, qi)
            print(p, q)
            circuits.append([p, q])
            djntset[p] = len(circuits) - 1
            djntset[q] = len(circuits) - 1
            print(circuits)
            print()

        elif pi == -1:
            print(pi, qi)
            print(p, q)
            circuits[qi].append(p)
            djntset[p] = qi
            lastBoxes = (p, q)
            print(circuits)
            print()
        elif qi == -1:
            print(pi, qi)
            print(p, q)
            circuits[pi].append(q)
            djntset[q] = pi
            lastBoxes = (p, q)
            print(circuits)
            print()

        

    print(lastBoxes)
    sizes = set(map(len, circuits))
    print(sizes)
    print(math.prod(sizes))

s1()


            

    
    
    
    

