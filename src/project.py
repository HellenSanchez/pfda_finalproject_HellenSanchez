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
    segment_height = SCREEN_HEIGHT // number
    for i in range(number):
        attempts = 0
        while attempts < 1000:
            attempts += 1
            side = random.choice(['left', 'right'])
            if side == 'left':
                x = random.randint(0, 10)
            else:
                x = random.randint(SCREEN_WIDTH - tree_width - 10, SCREEN_WIDTH - tree_width)
            y = random.randint(i * segment_height, (i + 1) * segment_height - 1)
            if all(abs(x - tx) > tree_width for tx, ty in tree_positions):
                tree_positions.append([x, y])
                break
    return tree_positions

def create_grass(number):
    grass_positions = []
    segment_height = SCREEN_HEIGHT // number
    for i in range(number):
        side = random.choice(['left', 'right'])
        if side == 'left':
            x = random.randint(GREEN_LEFT_ZONE[0], GREEN_LEFT_ZONE[1])
        else:
            x = random.randint(GREEN_RIGHT_ZONE[0], SCREEN_WIDTH)
        y = random.randint(i * segment_height, (i + 1) * segment_height - 1)
        color = random.choice(GREEN_TONES)
        size = random.randint(GRASS_MIN_SIZE, GRASS_MAX_SIZE)
        blades = []
        for j in range(size * 2):
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-size*3, 0)
            blades.append((offset_x, offset_y))
        grass_positions.append([x, y, color, blades])
    return grass_positions

def move_car(car_hitbox, keys):
    if keys[pygame.K_LEFT] and car_hitbox.left > 50:
        car_hitbox.x -= 5
    if keys[pygame.K_RIGHT] and car_hitbox.right < 350:
        car_hitbox.x += 5

def move_obstacles(obstacles, car_hitbox, score, game_over, speed):
    if game_over:
        return True, score
    for obs in obstacles:
        obs.y += speed
        if obs.y > SCREEN_HEIGHT:
            obs.y = random.randint(-200, -20)
            obs.x = random.choice(LANES)
            score += 1
        if car_hitbox.colliderect(obs):
            return False, score
    return True, score

def move_trees(tree_positions, tree_width, game_over, speed):
    if game_over:
        return
    for i, pos in enumerate(tree_positions):
        pos[1] += speed
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

def move_grass(grass_positions, game_over, speed):
    if game_over:
        return
    for pos in grass_positions:
        pos[1] += speed
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

def draw_screen(screen, car_image, cone_image, tree_image, car_hitbox, obstacles, font, score, line_positions, tree_positions, grass_positions, game_over):
    screen.fill((34, 139, 34))
    pygame.draw.rect(screen, (50, 50, 50), (50, 0, 300, SCREEN_HEIGHT))
    draw_grass(screen, grass_positions)
    for i in range(len(line_positions)):
        pygame.draw.line(screen, (255, 255, 255), (200, line_positions[i]), (200, line_positions[i] + 20), 4)
    for obs in obstacles:
        screen.blit(cone_image, (obs.x - 7, obs.y - 7))
    for pos in tree_positions:
        screen.blit(tree_image, (pos[0], pos[1]))
    screen.blit(car_image, (car_hitbox.x - 15, car_hitbox.y - 15))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_lines = [
            "Oops! You hit a cone!",
            "Press SPACE to restart",
            "Press ESC to quit"
        ]
        rect_width = 280
        rect_height = 90
        rect_x = (SCREEN_WIDTH - rect_width) // 2
        rect_y = 140
        pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))
        for i, line in enumerate(game_over_lines):
            text_surface = font.render(line, True, (255, 255, 255))
            text_x = rect_x + 20
            text_y = rect_y + 10 + i*25
            screen.blit(text_surface, (text_x, text_y))

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
    font = pygame.font.SysFont(None, 24)
    obstacles = create_obstacles(5)
    tree_positions = create_trees(6, tree_width)
    grass_positions = create_grass(GRASS_COUNT)
    score = 0
    game_over = False
    running = True
    line_positions = [i * 40 for i in range(12)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if score >= 20:
            speed = 6
        else:
            speed = OBSTACLE_SPEED
        if not game_over:
            move_car(car_hitbox, keys)
            move_trees(tree_positions, tree_width, game_over, speed)
            move_grass(grass_positions, game_over, speed)
            for i in range(len(line_positions)):
                line_positions[i] += speed
                if line_positions[i] > SCREEN_HEIGHT:
                    line_positions[i] -= len(line_positions) * 40
        running_obstacles, score = move_obstacles(obstacles, car_hitbox, score, game_over, speed)
        if not running_obstacles:
            game_over = True
        if game_over and keys[pygame.K_SPACE]:
            obstacles = create_obstacles(5)
            tree_positions = create_trees(6, tree_width)
            grass_positions = create_grass(GRASS_COUNT)
            car_hitbox.x = 180
            car_hitbox.y = 330
            score = 0
            game_over = False
        draw_screen(screen, car_image, cone_image, tree_image, car_hitbox, obstacles, font, score, line_positions, tree_positions, grass_positions, game_over)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
