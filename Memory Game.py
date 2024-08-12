import pygame,sys,random
pygame.init()
width,height = 400,400
screen = pygame.display.set_mode((width,height))

for i in range(5):
    pygame.draw.line(screen,(255,255,255),(width//5 * i,0),(width//5 * i,height))
    pygame.draw.line(screen,(255,255,255),(0,height//5 * i),(width,height//5 * i))

generatesquare=True
hidesquare=False
squares=[]
corrects=0
clicks=0
i=0
while True:
    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if clicks+1 < len(squares):
                x,y = event.pos
                if squares[clicks][0]<=x<=squares[clicks][0]+width//5 and squares[clicks][1]<=y<=squares[clicks][1]+height//5:
                    
                    clicks+=1
            else:
                corrects+=1
                generatesquare=True
                clicks=0
    if hidesquare:


        pygame.draw.rect(screen,(255,0,0),((squares[i][0]+2,squares[i][1]+2),(width//5-2,height//5-2)))
        if i+1 < len(squares):
            i+=1
            generatesquare=True
        else:
            i=0
        hidesquare=False
    if generatesquare:
        if len(squares)<=corrects:
            sx,sy = random.randint(0,4)*width//5, random.randint(0,4)*height//5
            squares.append([sx,sy])
        else:


            pygame.draw.rect(screen,(255,0,0),((squares[i][0]+2,squares[i][1]+2),(width//5-2,height//5-2)))
            generatesquare=False
            hidesquare=True
    pygame.display.update()