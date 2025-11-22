import pygame
import sys

# 12-1
def blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("12-1 Blue Sky")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((135, 206, 250))
        pygame.display.flip()
    pygame.quit()

# 12-2
class GameCharacter:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("character.bmp")
        self.rect = self.image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    def draw(self):
        self.screen.blit(self.image, self.rect)

def game_character():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("12-2 Game Character")
    character = GameCharacter(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((135, 206, 250))
        character.draw()
        pygame.display.flip()
    pygame.quit()

# 12-4
class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.speed = 5
    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen.get_height():
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen.get_width():
            self.rect.x += self.speed
    def draw(self):
        self.screen.blit(self.image, self.rect)

def rocket_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("12-4 Rocket")
    rocket = Rocket(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        rocket.move(keys)
        screen.fill((0, 0, 0))
        rocket.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# 12-5
def key_test():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("12-5 Keys")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(event.key)
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()

# 12-6
class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect(left=50, centery=screen.get_height() // 2)
        self.speed = 5
        self.bullets = []
    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen.get_height():
            self.rect.y += self.speed
    def shoot(self):
        bullet = pygame.Rect(self.rect.right, self.rect.centery-2, 10, 4)
        self.bullets.append(bullet)
    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.x += 10
            if bullet.x > self.screen.get_width():
                self.bullets.remove(bullet)
    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, (255, 0, 0), bullet)

def sideways_shooter():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("12-6 Sideways Shooter")
    ship = Ship(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
        keys = pygame.key.get_pressed()
        ship.move(keys)
        ship.update_bullets()
        screen.fill((0, 0, 0))
        ship.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
