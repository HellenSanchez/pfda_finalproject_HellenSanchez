import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

LANES = [80, 160, 240, 320]
GREEN_LEFT_ZONE = (0, 50)
GREEN_RIGHT_ZONE = (350, 400)
OBSTACLE_SPEED = 4

NEW_TREE_WIDTH = 80
GRASS_COUNT = 60
GRASS_MIN_SIZE = 2
GRASS_MAX_SIZE = 4

GREEN_TONES = [
    (0, 200, 0),
    (34, 139, 34),
]

def create_obstacles(number):
    obstacles = []
    for _ in range(number):
        x = random.choice(LANES)
        y = random.randint(-400, -20)
        obstacles.append(pygame.Rect(x, y, 25, 25))
    return obstacles

def create_trees(number, tree_width):
    tree_positions = []
    attempts = 0
    while len(tree_positions) < number and attempts < 1000:
        attempts += 1
        side = random.choice(['left', 'right'])
        if side == 'left':
            x = random.randint(0, 10)
        else:
            x = random.randint(SCREEN_WIDTH - tree_width - 10, SCREEN_WIDTH - tree_width)
        y = random.randint(-200, -50)
        if all(abs(x - tx) > tree_width for tx, ty in tree_positions):
            tree_positions.append([x, y])
    return tree_positions

def create_grass(number):
    grass_positions = []
    for _ in range(number):
        side = random.choice(['left', 'right'])
        if side == 'left':
            x = random.randint(GREEN_LEFT_ZONE[0], GREEN_LEFT_ZONE[1])
        else:
            x = random.randint(GREEN_RIGHT_ZONE[0], SCREEN_WIDTH)
        y = random.randint(-SCREEN_HEIGHT, 0)
        color = random.choice(GREEN_TONES)
        size = random.randint(GRASS_MIN_SIZE, GRASS_MAX_SIZE)
        blades = []
        for i in range(size * 2):
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-size*3, 0)
            blades.append((offset_x, offset_y))
        grass_positions.append([x, y, color, blades])
    return grass_positions

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
        obs.y += OBSTACLE_SPEED
        if obs.y > SCREEN_HEIGHT:
            obs.y = random.randint(-200, -20)
            obs.x = random.choice(LANES)
            score += 1
        if car_hitbox.colliderect(obs):
            print("Oops! You hit a cone")
            return False, score
    return True, score

def move_trees(tree_positions, tree_width):
    for i, pos in enumerate(tree_positions):
        pos[1] += OBSTACLE_SPEED
        if pos[1] > SCREEN_HEIGHT:
            attempts = 0
            while attempts < 1000:
                attempts += 1
                side = random.choice(['left', 'right'])
                if side == 'left':
                    max_x = max(GREEN_LEFT_ZONE[0], GREEN_LEFT_ZONE[1] - tree_width)
                    new_x = random.randint(GREEN_LEFT_ZONE[0], max_x)
                else:
                    min_x = min(GREEN_RIGHT_ZONE[1] - tree_width, GREEN_RIGHT_ZONE[0])
                    new_x = random.randint(min_x, GREEN_RIGHT_ZONE[1] - tree_width)
                if all(abs(new_x - tree_positions[j][0]) > tree_width for j in range(len(tree_positions)) if j != i):
                    pos[0] = new_x
                    pos[1] = random.randint(-80, -20)
                    break

def move_grass(grass_positions):
    for pos in grass_positions:
        pos[1] += OBSTACLE_SPEED
        if pos[1] > SCREEN_HEIGHT:
            side = random.choice(['left', 'right'])
            pos[1] = random.randint(-50, -10)
            if side == 'left':
                pos[0] = random.randint(GREEN_LEFT_ZONE[0], GREEN_LEFT_ZONE[1])
            else:
                pos[0] = random.randint(GREEN_RIGHT_ZONE[0], SCREEN_WIDTH)

def draw_grass(screen, grass_positions):
    for pos in grass_positions:
        x, y, color, blades = pos
        for offset_x, offset_y in blades:
            pygame.draw.line(screen, color, (x + offset_x, y), (x + offset_x, y + offset_y))

def draw_screen(screen, car_image, cone_image, tree_image, car_hitbox, obstacles, font, score, line_positions, tree_positions, grass_positions):
    screen.fill((34, 139, 34))
    pygame.draw.rect(screen, (50, 50, 50), (50, 0, 300, SCREEN_HEIGHT))
    draw_grass(screen, grass_positions)
    for i in range(len(line_positions)):
        pygame.draw.line(screen, (255, 255, 255), (200, line_positions[i]), (200, line_positions[i] + 20), 4)
        line_positions[i] += OBSTACLE_SPEED
        if line_positions[i] > SCREEN_HEIGHT:
            line_positions[i] -= len(line_positions) * 40
    for pos in tree_positions:
        screen.blit(tree_image, (pos[0], pos[1]))
    screen.blit(car_image, (car_hitbox.x - 15, car_hitbox.y - 15))
    for obs in obstacles:
        screen.blit(cone_image, (obs.x - 7, obs.y - 7))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pixel Racing Car")
    clock = pygame.time.Clock()
    car_image = pygame.image.load("Pixel_Racing_Car.png")
    car_image = pygame.transform.scale(car_image, (80, 90))
    car_hitbox = pygame.Rect(180, 330, 50, 60)
    cone_image = pygame.image.load("Traffic_Cone.png")
    cone_image = pygame.transform.scale(cone_image, (40, 40))
    tree_image = pygame.image.load("Tree.png")
    original_width, original_height = tree_image.get_size()
    new_height = int(original_height * (NEW_TREE_WIDTH / original_width))
    tree_image = pygame.transform.scale(tree_image, (NEW_TREE_WIDTH, new_height))
    tree_width = tree_image.get_width()
    font = pygame.font.SysFont(None, 30)
    obstacles = create_obstacles(5)
    tree_positions = create_trees(6, tree_width)
    grass_positions = create_grass(GRASS_COUNT)
    score = 0
    running = True
    line_positions = [i * 40 for i in range(12)]
    while running:
        running_events = handle_events()
        keys = pygame.key.get_pressed()
        move_car(car_hitbox, keys)
        move_trees(tree_positions, tree_width)
        move_grass(grass_positions)
        running_obstacles, score = move_obstacles(obstacles, car_hitbox, score)
        running = running_events and running_obstacles
        draw_screen(screen, car_image, cone_image, tree_image, car_hitbox, obstacles, font, score, line_positions, tree_positions, grass_positions)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()