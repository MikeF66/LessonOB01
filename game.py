import pygame
import sys

pygame.init()

def draw_text(surf, text, size, x, y):   #Рендерим текст
    font = pygame.font.SysFont(None, size)  # размер шрифта
    text_surface = font.render(text, True, (255, 255, 255))  # Белый цвет текста
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Новая игра")

speed = 3
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
fps = 60

paddle1_width, paddle1_height = 10, 100
paddle1_x = 40
paddle1_y = (screen_height - paddle1_height) // 2
paddle2_width, paddle2_height = 10, 100
paddle2_x = screen_width - paddle2_width - 40
paddle2_y = (screen_height - paddle2_height) // 2

# Параметры мяча
ball_radius = 8
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = -3

goal1 = 0
goal2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and 0 < paddle1_y < screen_height - paddle1_height + 3 * speed:
        paddle1_y -= speed
    if keys[pygame.K_z] and -3 * speed < paddle1_y < screen_height - paddle1_height:
        paddle1_y += speed
    if keys[pygame.K_UP] and 0 < paddle2_y < screen_height - paddle2_height + 3 * speed:
        paddle2_y -= speed
    if keys[pygame.K_DOWN] and -3 * speed < paddle2_y < screen_height - paddle2_height:
        paddle2_y += speed

    if ball_y <= 0:  # Столкновение с верхним и нижним краями экрана
        ball_speed_y = 3
    if ball_y >= screen_height:
        ball_speed_y = -3

    if ball_x <= 0:  # Пропуск мячей
        goal2 += 1
        paddle1_x = 40 # cброс мяча после гола
        paddle1_y = (screen_height - paddle1_height) // 2
        ball_x = screen_width // 2
        ball_y = 0
        ball_speed_x = -ball_speed_x

    if ball_x >= screen_width:
        goal1 += 1
        paddle2_x = screen_width - paddle2_width - 40  # cброс мяча после гола
        paddle2_y = (screen_height - paddle2_height) // 2
        ball_x = screen_width // 2
        ball_y = 0
        ball_speed_x = -ball_speed_x

    # Столкновение с платформой
    if paddle1_y <= ball_y <= paddle1_y + paddle1_height and paddle1_x <= ball_x <= paddle1_x + paddle1_width:
        ball_speed_x = -ball_speed_x
    if (paddle2_y <= ball_y <= paddle2_y + paddle2_height
            and paddle2_x <= ball_x + ball_radius <= paddle2_x + paddle2_width):
        ball_speed_x = -ball_speed_x

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle1_width, paddle1_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle2_width, paddle2_height))
    draw_text(screen, f'1-й игрок', 18, 300, 8)  # голы paddle1
    draw_text(screen, f'{goal1}', 36, 320, 30)  # голы paddle1
    draw_text(screen, f'2-й игрок', 18, 440, 8)  # голы paddle2
    draw_text(screen, f'{goal2}', 36, 460, 30)  # голы paddle2

    pygame.display.flip()


clock.tick(fps)
pygame.quit()
sys.exit()

