def s1():
    m = []
    with open('./inputs/d07.txt') as f:
        while l:= f.readline():
            m.append(list(l.strip()))
    
    total = 1
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == '^':
                m[i][j] = 1
            else:
                m[i][j] = 0
    
    print(list(enumerate(m)))
    for i in range(len(m)-2, 2, -2):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                if m[i-2][j+1] == 1:
                    total +=1
                    print(j)
                elif m[i-2][j-1] == 1:
                    total +=1
                    print(j)
                else:
                    for ii in range(i-4, 2, -2):
                        print(m[i][j],ii, i, j)
                        if m[ii][j] == 1:
                            break
                        elif m[ii][j+1] == 1:
                            total+=1
                        elif m[ii][j-1] == 1:
                            total+=1
                        

                
    
    print(total)
s1()