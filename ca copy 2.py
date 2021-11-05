import pygame, random, copy
pygame.init()
size = 75
wSize = 500
scale = round(wSize/size)
scr=pygame.display.set_mode((wSize,wSize))
cd = []
for y in range(size):
    cd.append([])
    for x in range(size):
        cd[y].append(random.choice([0, 0, 0, 0, 1, 0, 0, 0]))
clock = pygame.time.Clock()
game_over=False
drag = False
col = 2
def contains(l, x):
    for i in l:
        if i==x:return True
    return False
def only(l, x):
    for i in l:
        if i!=x:return False
    return True
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_q:
                col=1
            if event.key == pygame.K_w:
                col=2
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
        if event.type == pygame.MOUSEMOTION and drag == True:
            (mx, my) = pygame.mouse.get_pos()
            mx = int(mx/scale)
            my = int(my/scale)
            cd[mx][my] = col
    temp=copy.deepcopy(cd)
    for y in range(size):
        for x in range(size):
            c = min(1, max(0, cd[y][x]-1))*255#change -1 to 0.5, to see values of 1
            pygame.draw.rect(scr, (c, c, c), (y*scale, x*scale, scale, scale))
            nbhd = []
            for iy in range(-1, 2):
                for ix in range(-1, 2):
                    if [ix, iy]!=[0, 0]: nbhd.append(cd[(y+iy)%size][(x+ix)%size])
            c=cd[y][x]
            if c==1:
                if only(nbhd, 0) or contains(nbhd, 1):#if neighborhood is 0 or 1 only
                    ry=random.randint(-1, 1)#y shift of random neighbor
                    rx= random.randint(-1, 1)#x shift of random neighbor
                    temp[y][x], temp[(y+ry)%size][(x+rx)%size] = temp[(y+ry)%size][(x+rx)%size], temp[y][x]#swap places with neighboor
                else:temp[y][x]=2#if it encounters a cell that isnt 1 or 0 it turns to 2
            #if c>1:temp[y][x]=round(temp[y][x]-0.1, 1)
            #if c!=1 and c!=2 and c!=0:print(c)
    pygame.display.update()
    cd=temp
    #clock.tick(10)
