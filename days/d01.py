import os
def star1():
    with open('./inputs/d01.txt', 'r') as f:
        global starting
        global count
        while l := f.readline():
            value = 0
            if l[0] == 'L':
                value = - int(l[1:])
            if l[0] == 'R':
                value = int(l[1:])

            starting = (starting + value) % 100
            if starting == 0:
                count+=1
def star2():
    global starting
    global count
    with open('./inputs/d01_test.txt', 'r') as f:
        while l := f.readline():
            value = (-1 if l[0] == 'L' else 1) * int(l[1:])

            
            if value not in range(-99, 100):
                count+= abs(value) // 100
                value = value % 100

            sv = starting + value

            if (starting + value) % 100 == 0:
                count+=1

            elif (starting + value) not in range(0, 100) and (starting + value) % 100 != 0:
                count += 1

            starting = sv % 100
            print('starting', starting, count)

#starting = 50
#count = 0
#star1()
#print(count)
starting = 50
count = 0
star2()
print(count)
