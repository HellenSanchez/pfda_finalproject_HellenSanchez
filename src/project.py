import pygame
import random

def create_obstacles(number):
    obstacles = []
    for _ in range(number):
        x = random.randint(0, 380)
        y = random.randint(0, 200)
        obstacles.append(pygame.Rect(x, y, 20, 20))
    return obstacles

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_car(car, keys):
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= 5
    if keys[pygame.K_RIGHT] and car.right < 400:
        car.x += 5

def move_obstacles(obstacles, car, score):
    for obs in obstacles:
        obs.y += 4
        if obs.y > 400:
            obs.y = random.randint(-200, -20)
            obs.x = random.randint(0, 380)
            score += 1
        if car.colliderect(obs):
            print("Oops! You hit a cone")
            return False, score
    return True, score

def draw_screen(screen, car_image, car, obstacles, font, score):
    screen.fill((0, 0, 0))
    screen.blit(car_image, (car.x, car.y))
    for obs in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obs)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Pixel Racing Car")
    clock = pygame.time.Clock()

    car_image = pygame.image.load("Pixel_Racing_Car.png")
    car_image = pygame.transform.scale(car_image, (48, 54))
    car = car_image.get_rect()
    car.x = 180
    car.y = 330

    font = pygame.font.SysFont(None, 30)

    obstacles = create_obstacles(5)
    score = 0
    running = True

    while running:
        running_events = handle_events()
        keys = pygame.key.get_pressed()
        move_car(car, keys)

        running_obstacles, score = move_obstacles(obstacles, car, score)
        running = running_events and running_obstacles

        draw_screen(screen, car_image, car, obstacles, font, score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()