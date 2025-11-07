import sys
import pygame
from node import *
from link import *

windows_w = 800
windows_h = 600
running = True

pygame.init()
display_sur = pygame.display.set_mode((windows_w, windows_h))
clock = pygame.time.Clock()
background = pygame.surface.Surface((windows_w, windows_h))

router1_image = "./graphic/router.png"
router1_pos = (150, 300)
router2_image = "./graphic/router.png"
router2_pos = (650, 300)
switch1_image = "./graphic/switch.png"
switch1_pos = (400, 300)

sprite_group = pygame.sprite.Group()
router1 = Node(router1_image, router1_pos, sprite_group)
router2 = Node(router2_image, router2_pos, sprite_group)
switch1 = Node(switch1_image, switch1_pos, sprite_group)
link1 = Link(router1, switch1, "black", 3)
link2 = Link(router2, switch1, "black", 3)


while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
    background.fill("white")
    display_sur.blit(background, (0, 0))
    link1.draw(display_sur)
    link2.draw(display_sur)
    sprite_group.draw(display_sur)
    sprite_group.update()
    pygame.display.flip()
    clock.tick(60)