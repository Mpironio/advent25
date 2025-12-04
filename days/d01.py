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
    with open('./inputs/d01.txt', 'r') as f:
        while l := f.readline():
            value = (-1 if l[0] == 'L' else 1) * int(l[1:])
         #   print('starting', starting, value, count)
            bw = (starting + value < 0 or starting + value > 99) and starting != 0 
            if value not in range(-99, 100):
                count+= abs(value) // 100
         #       print('loops', abs(value) // 100, value % 100, f"{starting} + {value%100} = {starting + value%100}")



                value = value % 100 - 100 if value < 0 else value % 100

                bw = (starting + value < 0 or starting + value > 99) and starting != 0
            
            if bw:
               count += 1


            elif (starting + value) % 100 == 0:
                count+=1


            
            starting = (starting + value) % 100

starting = 50
count = 0
star1()
print(count)
starting =50 
count = 0
star2()
print(count)
