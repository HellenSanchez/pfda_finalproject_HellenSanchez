import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
car = pygame.Rect(190, 360, 20, 40)
obstacles = []

for _ in range(5):
    x = random.randint(0, 380)
    y = random.randint(0, 200)
    obstacles.append(pygame.Rect(x, y, 20, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= 5
    if keys[pygame.K_RIGHT] and car.right < 400:
        car.x += 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), car)
    for obs in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obs)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
