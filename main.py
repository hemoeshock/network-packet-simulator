import sys
import pygame
from node import *
from link import *
from packet import *

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
packets_group = pygame.sprite.Group()
router1 = Node(router1_image, router1_pos, sprite_group)
router2 = Node(router2_image, router2_pos, sprite_group)
switch1 = Node(switch1_image, switch1_pos, sprite_group)
link1 = Link(router1, switch1, "black", 3)
link2 = Link(router2, switch1, "black", 3)
link1.draw(display_sur)
link2.draw(display_sur)

packet1 = Packet(link1, packets_group)

'''just for test
background_fill_router = pygame.Surface((router1.rect.width,router1.rect.height))
background_fill_router .fill('yellow')

background_fill_switch = pygame.Surface((switch1.rect.width,switch1.rect.height))
background_fill_switch .fill('yellow')'''


while running:
    dt = clock.tick(60)/1000
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
    background.fill("white")
    display_sur.blit(background, (0, 0))
    '''just for test
    display_sur.blit(background_fill_router,(router1.rect))
    display_sur.blit(background_fill_switch,(switch1.rect))'''
    link1.draw(display_sur)
    link2.draw(display_sur)
    sprite_group.draw(display_sur)
    packets_group.draw(display_sur)
    packets_group.update(dt)
    sprite_group.update()
    pygame.display.flip()
    clock.tick(60)