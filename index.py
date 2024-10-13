import pygame
pygame.init()

winWidth = 852
winHeight = 480

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("game")

walkRight = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
walkLeft = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')

clock = pygame.time.Clock()

x = 0
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False 
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        win.blit(walkLeft[walkCount//3] , (x, y))
        walkCount += 1
    
    elif right: 
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    
    else:
        win.blit(char, (x, y))
    
    pygame.display.update()

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < winWidth - width - vel:
        x += vel
        left = False
        right = True

    else:
        right = False
        left = False
        walkCount = 0
    
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()