
def star1():
    with open('d01.txt', 'r') as f:
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
    with open('d01.txt', 'r') as f:
        while l := f.readline():
            value = 0
            
            if l[0] == 'L':
                value = - int(l[1:])
            if l[0] == 'R':
                value = int(l[1:])
            #print('value ', value)
            sv = starting + value
            #print('sv ', starting, value)
            if value > 99 or value < -99:
                count+=abs(value//100)
                value = value % 100
            if starting != 0 and (sv > 99 or sv < 0):
                count+=1
             #   print('count: ', count)
            starting = (starting + value) % 100
            #print('st' + str(starting))
            if starting == 0:
                count+=1
             #   print('count: ', count)

starting = 50
count = 0
star2()
print(count)
