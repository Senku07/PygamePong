import pygame
import random

pygame.init()

Window_Width = 800
Window_Height = 600

WIN = pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption("Pong P")

Paddle_Width = 20
Paddle_Height = 100
Paddle_Color = (255,45,255)
Paddle_Speed = 5

player_paddle = pygame.Rect(50,(Window_Height-Paddle_Height)/2,Paddle_Width,Paddle_Height)
opponent_paddle = pygame.Rect(Window_Width-50-Paddle_Width,(Window_Height-Paddle_Height)/2,Paddle_Width,Paddle_Height)

Ball_Width = 20
Ball_Height = 20
Ball_Color = (34,56,89)
Ball_Speed = 2

ball = pygame.Rect((Window_Width - Ball_Width)/2,(Window_Height - Ball_Height)/2,Ball_Width,Ball_Height)

ball_dir_x = random.choice([1,-1])
ball_dir_y = random.choice([1,-1])

Player_Score = 0
Oppenent_Score = 0
font = pygame.font.Font(None,50)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    WIN.fill((0,0,0))
    score_text = font.render(str(Player_Score)+":"+str(Oppenent_Score),True,(255,255,255))
    WIN.blit(score_text,(50,10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.y -= Paddle_Speed
    if keys[pygame.K_DOWN]:
        player_paddle.y += Paddle_Speed
    
    if ball.y < opponent_paddle.y + Paddle_Height / 2:
        opponent_paddle.y -= Paddle_Speed
    if ball.y > opponent_paddle.y + Paddle_Height / 2:
        opponent_paddle.y += Paddle_Speed
    
    ball.x += ball_dir_x * Ball_Speed
    ball.y += ball_dir_y * Ball_Speed

    if ball.top <= 0 or ball.bottom >= Window_Height:
        ball_dir_y *= -1
    if ball.left <= 0:
        Oppenent_Score += 1
        ball_dir_x *= -1
        ball.x = (Window_Width - Ball_Width)/2
        ball.y = (Window_Height - Ball_Height)/2
    
    if ball.right >= Window_Width:
        Player_Score += 1
        ball_dir_x *= -1
        ball.x = (Window_Width - Ball_Width)/2
        ball.y = (Window_Height - Ball_Height)/2
    
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_dir_x *= -1
    


    pygame.draw.rect(WIN,Paddle_Color,player_paddle)
    pygame.draw.rect(WIN,Paddle_Color,opponent_paddle)
    pygame.draw.ellipse(WIN,Ball_Color,ball)

    # player




