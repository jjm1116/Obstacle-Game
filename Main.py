import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Obstacle Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player setup
player_radius = 25
player = pygame.Rect(300 - player_radius, 200 - player_radius, player_radius * 2, player_radius * 2)
speed = 10
stage = 0

# Define stages with varying obstacles, time limits, and names
stages = [
    {"name": "easy", "num_obstacles": 3, "time_limit": 60000},  # time in ms(milleseconds)
    {"name": "medium", "num_obstacles": 4, "time_limit": 50000},
    {"name": "hard", "num_obstacles": 5, "time_limit": 40000},
    {"name": "insane", "num_obstacles": 6, "time_limit": 30000},
    {"name": "expert", "num_obstacles": 7, "time_limit": 20000},
    {"name": "mad", "num_obstacles": 8, "time_limit": 15000},
    {"name": "shenanigans", "num_obstacles": 8, "time_limit": 13000},
    {"name": "crazy", "num_obstacles": 8, "time_limit": 10000},
    {"name": "Final Exam", "num_obstacles": 8, "time_limit": 8000},
    {"name": "asian", "num_obstacles": 9, "time_limit": 5000},
    {"name": "???", "num_obstacles": 10, "time_limit": 4000},
]

# Target setup
target = pygame.Rect(random.randint(0, 550), random.randint(0, 350), 50, 50)

# Function to generate obstacles
def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            obstacle = pygame.Rect(random.randint(0, 550), random.randint(0, 350), 50, 50)
            if not player.colliderect(obstacle) and not target.colliderect(obstacle):
                obstacles.append(obstacle)
                break
    return obstacles

# Initialize stage-related variables
current_stage = stages[stage]
time_limit = current_stage["time_limit"]
time_left = time_limit
obstacles = generate_obstacles(current_stage["num_obstacles"])

# Grace period settings
grace_period = 600  # 600 ms
grace_timer = grace_period

# Font setup
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
running = True
clock = pygame.time.Clock()

def show_end_screen(message):
    """Display the end screen with replay and quit options."""
    while True:
        screen.fill(WHITE)

        # Display message
        text = large_font.render(message, True, BLACK)
        screen.blit(text, (300 - text.get_width() // 2, 100))

        # Draw buttons
        replay_button = pygame.Rect(200, 200, 200, 50)
        quit_button = pygame.Rect(200, 270, 200, 50)
        pygame.draw.rect(screen, GREEN, replay_button)
        pygame.draw.rect(screen, RED, quit_button)

        replay_text = font.render("Replay", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        screen.blit(replay_text, (300 - replay_text.get_width() // 2, 215))
        screen.blit(quit_text, (300 - quit_text.get_width() // 2, 285))

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    return True  # Replay
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

# Main game loop
while running:
    start_time = pygame.time.get_ticks()
    while running:
        dt = clock.tick(30)  # Delta time (ms)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.top > 0:
            player.y -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.bottom < 400:
            player.y += speed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.left > 0:
            player.x -= speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.right < 600:
            player.x += speed

        # Check collision with target
        if grace_timer <= 0 and player.colliderect(target):
            stage += 1
            if stage >= len(stages):
                if show_end_screen("You Win! Replay?"):
                    # Reset game variables
                    stage = 0
                    current_stage = stages[stage]
                    time_limit = current_stage["time_limit"]
                    time_left = time_limit
                    player.topleft = (300 - player_radius, 200 - player_radius)
                    obstacles = generate_obstacles(current_stage["num_obstacles"])
                    grace_timer = grace_period
                else:
                    running = False
                    break

            # Progress to the next stage
            current_stage = stages[stage]
            time_limit = current_stage["time_limit"]
            time_left = time_limit
            target.x = random.randint(0, 550)
            target.y = random.randint(0, 350)
            obstacles = generate_obstacles(current_stage["num_obstacles"])
            grace_timer = grace_period

        # Check collision with obstacles
        if grace_timer <= 0:
            for obstacle in obstacles:
                if player.colliderect(obstacle):
                    if show_end_screen("Game Over! Replay?"):
                        # Reset game variables
                        stage = 0
                        current_stage = stages[stage]
                        time_limit = current_stage["time_limit"]
                        time_left = time_limit
                        player.topleft = (300 - player_radius, 200 - player_radius)
                        obstacles = generate_obstacles(current_stage["num_obstacles"])
                        grace_timer = grace_period
                    else:
                        running = False
                    break

        # Decrement timers
        if grace_timer > 0:
            grace_timer -= dt  # Reduce grace period by delta time

        time_left -= dt
        if time_left <= 0:
            if show_end_screen("Time's up! Replay?"):
                # Reset game variables
                stage = 0
                current_stage = stages[stage]
                time_limit = current_stage["time_limit"]
                time_left = time_limit
                player.topleft = (300 - player_radius, 200 - player_radius)
                obstacles = generate_obstacles(current_stage["num_obstacles"])
                grace_timer = grace_period
            else:
                running = False
            break

        # Draw everything
        screen.fill(WHITE)

        # Draw aura during grace period
        if grace_timer > 0:
            aura_radius = player_radius + 15
            aura_center = (player.centerx, player.centery)
            color_value = int(255 * (grace_timer / grace_period))
            pygame.draw.circle(screen, (0, 0, color_value), aura_center, aura_radius)

        # Draw player, target, and obstacles
        pygame.draw.circle(screen, BLUE, player.center, player_radius)
        pygame.draw.rect(screen, RED, target)

        for obstacle in obstacles:
            pygame.draw.rect(screen, BLACK, obstacle)

        # Display stage and time left
        stage_name = current_stage["name"]
        stage_text = font.render(f"Stage: {stage + 1} ({stage_name})", True, BLACK)
        time_text = font.render(f"Time: {time_left // 1000}", True, BLACK)
        screen.blit(stage_text, (10, 10))
        screen.blit(time_text, (500, 10))

        pygame.display.flip()

pygame.quit()
