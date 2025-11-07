import pygame

class Node(pygame.sprite.Sprite):
    def __init__(self, image, pos, *groups):
        super().__init__(groups)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_frect(center=pos)

        self.dragging = False
        self.mouse_offset = (0, 0)

    def drag_move(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]

        # Start dragging only on first click
        if left_click and not self.dragging and self.rect.collidepoint(mouse_pos):
            self.dragging = True
            # Keep mouse offset
            self.mouse_offset = (self.rect.centerx - mouse_pos[0],
                                 self.rect.centery - mouse_pos[1])

        # Stop dragging when mouse released
        if not left_click:
            self.dragging = False

        # While dragging
        if self.dragging:
            self.rect.center = (mouse_pos[0] + self.mouse_offset[0],
                                mouse_pos[1] + self.mouse_offset[1])

    def update(self):
        self.drag_move()
