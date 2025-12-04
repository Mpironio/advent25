from itertools import permutations 
total = 0

def s1():
    global total

    with open('inputs/d03.txt') as f:
        while l:= f.readline():
            bgst = 0
            sndbgst = 0
            nums = list(map(lambda e: int(e), list(l.strip())))
           
            max = 0
            for i, v1 in enumerate(nums):
                for j, v2 in enumerate(nums):
                    if i >= j: continue
                    partial = int(str(v1) + str(v2)) 
                    if partial > max:
                        max = partial

            total += max

        print(total)

def s2():
    global total
    with open('inputs/d03_test.txt') as f:
        while l:= f.readline():
            nums = list(map(lambda e: int(e), list(l.strip())))
            ons = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
            max = 0
            for p in set(permutations(ons)):
                asd = list(filter((lambda i: ons[i] > 0), ons))
                print(asd)
                break
            break
                
s1()
s2()
