import sys

# a cloth of size sizeXsize will be generated; size must be odd
if len(sys.argv) == 2:
    size = int(sys.argv[1])
else:
    size = 11

if size % 2 == 0:
    print "warning: size must be odd; incrementing by 1 to fix"
    size += 1

shift = (size-1)/2 # shift coordinates: (0,0) @ corner -> (0,0) at origin
cloth = [[0]*size for i in range(size)] # initialize cloth


# generate list of odd squares
squares = []
for i in range(1,size+1,2): squares.append(i**2)
#print squares


# define some vars
ring = 0
ringTmp = 0
x = 0
y = 0


# define directions enumerator
up = 1
down = 2
left = 3
right = 4
direction = up


# generate cloth
for i in range(1,squares[-1]+1):
    
    #print i,x,y # print coordinates of ulam number

    # DEFINE WHAT TO BE PRINTED:
    ############################
    cloth[shift-y][x+shift] = i
    #if i % (ring+1) == 0: cloth[shift-y][x+shift] = 0
    #if i % (ring+2) == 0: cloth[shift-y][x+shift] = 0
    #if i % 3 == 0: cloth[shift-y][x+shift] = 0
    #if i % 4 == 0: cloth[shift-y][x+shift] = 0
    #else: cloth[shift-y][x+shift] = ""
    ###########################

    # if we are at an odd square, we must proceed to next ring
    if i in squares:
        ring += 1
        direction = up

    # if we are at a ring's corner, we must turn
    if abs(x)==ring and abs(y)==ring and ring!=0:
        if x<0 and y>0: direction = down
        elif x<0 and y<0: direction = right
        elif x>0 and y<0: direction = up
        elif x>0 and y>0: direction = left

    # modify x and y according to this iteration's direction
    if direction==left: x -= 1
    elif direction==right: x += 1
    elif direction==down: y -= 1
    elif direction==up: y += 1

    # if we have just moved into a new ring, the next direction will be left
    if ring != ringTmp:
        direction = left
        ringTmp = ring


# determine padding: how much space each number printed has
padding = 1
while squares[-1] > 10**(padding-1): padding += 1
#padding = 2 # override (useful if just printing single digits)

    
# print cloth
print('\n'.join([''.join([("{:"+str(padding)+"}").format(item) for item in row]) 
      for row in cloth]))
