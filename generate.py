
size = 41
shift = (size-1)/2
cloth = [[0]*size for i in range(size)]

sq = []
for i in range(1,size+1,2):
    sq.append(i**2)
print sq

ring = 0
ringTmp = 0
x = 0
y = 0
direction = "up"

for i in range(1,sq[-1]+1):
    
    print i,x,y

    #cloth[shift-y][x+shift] = i
    if i % (ring+3) == 0:
    #if i % (ring+1) == 0:
    #if i % 6 == 0:
        cloth[shift-y][x+shift] = 1
    else:
        cloth[shift-y][x+shift] = ""

    if i in sq:
        ring += 1
        direction = "up"

    if abs(x)==ring and abs(y)==ring and ring!=0:
        if x<0 and y>0: direction = "down"
        elif x<0 and y<0: direction = "right"
        elif x>0 and y<0: direction = "up"
        elif x>0 and y>0: direction = "left"

    if direction=="left": x -= 1
    elif direction=="right": x += 1
    elif direction=="down": y -= 1
    elif direction=="up": y += 1

    if ring != ringTmp:
        direction = "left"
        ringTmp = ring
    

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in cloth]))
