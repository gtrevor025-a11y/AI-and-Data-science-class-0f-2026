import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Man Mobile")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
GROUND_COLOR = (60, 180, 75)
PLAYER_COLOR = (50, 90, 200)
OBSTACLE_COLOR = (200, 60, 60)

# Ground
ground = pygame.Rect(0, 350, WIDTH, 50)

# Player
player = pygame.Rect(100, 290, 40, 60)
velocity_y = 0
gravity = 0.8
jump_strength = -15
on_ground = True

# Obstacles
obstacles = []
spawn_timer = 0

# Game state
speed = 7   # Start faster
score = 0
game_over = False


def spawn_obstacle():
    height = random.choice([40, 50, 60])
    obstacle = pygame.Rect(WIDTH, 350 - height, 30, height)
    obstacles.append(obstacle)


def reset_game():
    global obstacles, score, game_over, velocity_y, speed
    obstacles = []
    score = 0
    velocity_y = 0
    player.y = 290
    speed = 7
    game_over = False


while True:
    clock.tick(60)

    # -------- TOUCH INPUT --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                if on_ground:
                    velocity_y = jump_strength
                    on_ground = False
            else:
                reset_game()

    if not game_over:
        # -------- PLAYER PHYSICS --------
        velocity_y += gravity
        player.y += velocity_y

        if player.colliderect(ground):
            player.bottom = ground.top
            velocity_y = 0
            on_ground = True

        # -------- SPAWN OBSTACLES --------
        spawn_timer += 1
        if spawn_timer > max(45, 90 - speed * 3):
            spawn_obstacle()
            spawn_timer = 0

        # -------- MOVE OBSTACLES --------
        for obstacle in obstacles:
            obstacle.x -= speed

        obstacles = [obs for obs in obstacles if obs.right > 0]

        # -------- COLLISION --------
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                game_over = True

        # -------- INCREASE DIFFICULTY --------
        score += 1
        if score % 300 == 0:   # Every few seconds
            speed += 0.5       # Gradually faster

    # -------- DRAW --------
    screen.fill(WHITE)

    pygame.draw.rect(screen, GROUND_COLOR, ground)
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    score_text = font.render(f"Score: {score // 10}", True, (20, 20, 20))
    screen.blit(score_text, (10, 10))

    if game_over:
        over = font.render("Tap to Restart", True, (20, 20, 20))
        screen.blit(over, (WIDTH // 2 - 100, HEIGHT // 2 - 20))

    pygame.display.update()
