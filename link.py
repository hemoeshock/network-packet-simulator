import pygame

class Link:
     def __init__(self, node_a, node_b, color="black", width=3):
        self.node_a = node_a
        self.node_b = node_b
        self.color = color
        self.width = width

     def draw(self, display_sur):
        a = self.node_a.rect
        b = self.node_b.rect

        if a.centerx > b.centerx:
            start = a.midleft
            end   = b.midright
        else:
            start = a.midright
            end   = b.midleft

        pygame.draw.line(display_sur, self.color, start, end, self.width)