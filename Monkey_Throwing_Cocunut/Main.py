import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Catching Coconuts")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load monkey image
monkey_img = pygame.image.load("OIP.jpg")  # Adjusted path for monkey image
monkey_img = pygame.transform.scale(monkey_img, (80, 80))

# Load coconut image
coconut_img = pygame.image.load("Coconut.jpg")  # Adjusted path for coconut image
coconut_img = pygame.transform.scale(coconut_img, (40, 40))

# Monkey class
class Monkey:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 100
        self.width = 80
        self.height = 80
        self.speed = 10

    def draw(self):
        screen.blit(monkey_img, (self.x, self.y))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

# Coconut class
class Coconut:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 40)
        self.y = random.randint(-600, -40)
        self.speed = random.randint(3, 7)

    def draw(self):
        screen.blit(coconut_img, (self.x, self.y))

    def fall(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-600, -40)
            self.x = random.randint(0, SCREEN_WIDTH - 40)

# Main game loop
def main():
    monkey = Monkey()
    coconuts = [Coconut() for _ in range(7)]
    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            monkey.move("left")
        if keys[pygame.K_RIGHT]:
            monkey.move("right")

        # Update and draw coconuts
        for coconut in coconuts:
            coconut.fall()
            coconut.draw()

            # Check collision with monkey
            if (
                monkey.x < coconut.x + 40
                and monkey.x + monkey.width > coconut.x
                and monkey.y < coconut.y + 40
                and monkey.y + monkey.height > coconut.y
            ):
                score += 1
                coconut.y = random.randint(-600, -40)
                coconut.x = random.randint(0, SCREEN_WIDTH - 40)

        # Draw monkey
        monkey.draw()

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()