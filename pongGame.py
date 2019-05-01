import pygame, sys

FPS = 200
size = (800,240)
screen = pygame.display.set_mode(size)

def drawPaddle(paddle):
    pygame.draw.rect(screen, (255,255,255), paddle)

def drawBall(ball):
    pygame.draw.rect(screen, (255,255,255), ball)

def drawCentreLine():
    pygame.draw.rect(screen, (255,255,255), (395,24,10,20))
    pygame.draw.rect(screen, (255,255,255), (395,72,10,20))
    pygame.draw.rect(screen, (255,255,255), (395,120,10,20))
    pygame.draw.rect(screen, (255,255,255), (395,168,10,20))
    pygame.draw.rect(screen, (255,255,255), (395,216,10,20))

def moveBall(ball,ballX,ballY):
    ball.x += ballX
    ball.y += ballY
    return ball

def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == 10 or ball.bottom == 230:
        ballDirY = ballDirY * -1
    if ball.left == 10 or ball.right == 790:
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else:
        return 1

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    
    paddle1X = 20
    paddle1Y = 50
    paddle1 = pygame.Rect(paddle1X,paddle1Y,10,40)
    paddle2X = 780
    paddle2Y = 100
    paddle2 = pygame.Rect(paddle2X,paddle2Y,10,40)
    ballX = 35
    ballY = 60
    ball = pygame.Rect(ballX,ballY,10,10)

    ballDirX = -1
    ballDirY = -1
    
    drawCentreLine()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
                
        screen = pygame.display.set_mode(size)        
        drawCentreLine()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        ball = moveBall(ball,ballDirX,ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
