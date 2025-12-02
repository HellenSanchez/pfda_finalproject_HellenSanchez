import pygame
import random

def create_obstacles(number):
    obstacles = []
    for _ in range(number):
        x = random.randint(0, 370)
        y = random.randint(-200, -20)
        obstacles.append(pygame.Rect(x, y, 25, 25))
    return obstacles

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_car(car_hitbox, keys):
    if keys[pygame.K_LEFT] and car_hitbox.left > 0:
        car_hitbox.x -= 5
    if keys[pygame.K_RIGHT] and car_hitbox.right < 400:
        car_hitbox.x += 5

def move_obstacles(obstacles, car_hitbox, score):
    for obs in obstacles:
        obs.y += 4
        if obs.y > 400:
            obs.y = random.randint(-200, -20)
            obs.x = random.randint(0, 370)
            score += 1
        if car_hitbox.colliderect(obs):
            print("Oops! You hit a cone")
            return False, score
    return True, score

def draw_screen(screen, car_image, cone_image, car_hitbox, obstacles, font, score):
    screen.fill((0, 0, 0))
    screen.blit(car_image, (car_hitbox.x - 15, car_hitbox.y - 15))
    for obs in obstacles:
        screen.blit(cone_image, (obs.x - 7, obs.y - 7))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Pixel Racing Car")
    clock = pygame.time.Clock()

    car_image = pygame.image.load("Pixel_Racing_Car.png")
    car_image = pygame.transform.scale(car_image, (80, 90))
    car_hitbox = pygame.Rect(180, 330, 50, 60)

    cone_image = pygame.image.load("Traffic_Cone.png")
    cone_image = pygame.transform.scale(cone_image, (40, 40))

    font = pygame.font.SysFont(None, 30)

    obstacles = create_obstacles(5)
    score = 0
    running = True

    while running:
        running_events = handle_events()
        keys = pygame.key.get_pressed()
        move_car(car_hitbox, keys)

        running_obstacles, score = move_obstacles(obstacles, car_hitbox, score)
        running = running_events and running_obstacles

        draw_screen(screen, car_image, cone_image, car_hitbox, obstacles, font, score)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()