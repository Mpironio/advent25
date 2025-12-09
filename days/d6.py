import math
def fill_transpose(l):
    ml = len(max(l, key=len))



def s1():
    m = []
    with open('./inputs/d06_test.txt') as f:
        while l:= f.readline():
            m.append(l.strip().split())
    total = 0
    # print(len(m))
    # print(len(m[0]))

    for i in range(0, len(m[0])):
        a = int(m[0][i])
        b = int(m[1][i])
        c = int(m[2][i])
        d = int(m[3][i])
        op = m[4][i]
        # print(a,b,c, d,op)
        if op == '*':
            total+= a * b * c * d
        if op == '+':
            total+= a + b + c + d
            
    
    return total

def s2():
    m = []
    with open('./inputs/d06_test.txt') as f:
        while l:= f.readline():
            m.append(l)
    total = 0
    m2 = []
    
    # print(m)
    m2 = list(map(list, zip(*m[:-1])))[:-1]
    # print(m2)
    ops = m[-1].split()
    # print(ops)
    # print(len(m2))
    # print(ops)
    # print(len(list(filter(lambda ll: len(set(ll)) != 1, m2))))
    # print(m2)
    print(ops)
    j = 0
    nums = []
    m2.append([' '])
    for i in m2:
        print(i, nums, ops[j])
        num = ''.join(i)
        if num == '    ' or num == ' ':
            op = ops[j]
            if op == '+':
                total+=sum(nums)
            else:
                total+=math.prod(nums)
            nums=[]
            j+=1

        else:
            print(num)
            nums.append(int(num))
        
    

    return total




# print(s1())
print(s2())