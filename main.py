import pygame, sys, random

# set up screen
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mouse_pos = pygame.mouse.get_pos()
        self.image = pygame.Surface((10,10))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=(self.mouse_pos))
        self.timer = 0
    def update(self):
        self.timer += 1
        if self.timer >= 10:
            self.kill()
rect_group = pygame.sprite.Group()
def spawn_rect():
    rect = Rect()
    rect_group.add(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    spawn_rect()
    rect_group.update()
    rect_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
