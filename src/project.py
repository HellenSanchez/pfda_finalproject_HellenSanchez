import pygame
import random

def create_obstacles(number):
    obstacles = []
    for _ in range(number):
        x = random.randint(50, 325)
        y = random.randint(-200, -20)
        obstacles.append(pygame.Rect(x, y, 25, 25))
    return obstacles

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_car(car_hitbox, keys):
    if keys[pygame.K_LEFT] and car_hitbox.left > 50:
        car_hitbox.x -= 5
    if keys[pygame.K_RIGHT] and car_hitbox.right < 350:
        car_hitbox.x += 5

def move_obstacles(obstacles, car_hitbox, score):
    for obs in obstacles:
        obs.y += 4
        if obs.y > 400:
            obs.y = random.randint(-200, -20)
            obs.x = random.randint(50, 325)
            score += 1
        if car_hitbox.colliderect(obs):
            print("Oops! You hit a cone")
            return False, score
    return True, score

def draw_tree(screen, x, y):
    pygame.draw.rect(screen, (101, 67, 33), (x + 20, y + 40, 10, 20))
    pygame.draw.polygon(screen, (0, 100, 0), [(x + 25, y), (x, y + 40), (x + 50, y + 40)])

def move_trees(tree_positions):
    for pos in tree_positions:
        pos[1] += 4
        if pos[1] > 400:
            pos[1] = -80

def draw_screen(screen, car_image, cone_image, car_hitbox, obstacles, font, score, line_positions, tree_positions):
    screen.fill((34, 139, 34))
    pygame.draw.rect(screen, (50, 50, 50), (50, 0, 300, 400))
    for i in range(len(line_positions)):
        pygame.draw.line(screen, (255, 255, 255), (200, line_positions[i]), (200, line_positions[i] + 20), 4)
        line_positions[i] += 4
        if line_positions[i] > 400:
            line_positions[i] -= len(line_positions) * 40
    for pos in tree_positions:
        draw_tree(screen, pos[0], pos[1])
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
    tree_positions = [[random.choice([10, 340]), random.randint(-400, 400)] for _ in range(6)]
    score = 0
    running = True
    line_positions = [i * 40 for i in range(12)]

    while running:
        running_events = handle_events()
        keys = pygame.key.get_pressed()
        move_car(car_hitbox, keys)
        move_trees(tree_positions)
        running_obstacles, score = move_obstacles(obstacles, car_hitbox, score)
        running = running_events and running_obstacles

        draw_screen(screen, car_image, cone_image, car_hitbox, obstacles, font, score, line_positions, tree_positions)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()