import pygame
from pygame.math import Vector2


class Packet(pygame.sprite.Sprite):
    def __init__(self, link, *groups):
        super().__init__(*groups)

        self.link = link

        # Convert link start/end into Vector2
        self.start_pos = Vector2(self.link.start)
        self.end_pos   = Vector2(self.link.end)

        # Packet properties
        self.color = "red"
        self.radius = self.link.width + 2
        self.speed = 150      # pixels per second
        self.TTL = 0.2

        # Current position
        self.pos = Vector2(self.start_pos)

        # Create visual circle
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

        # Create rect for drawing
        self.rect = self.image.get_rect(center=self.pos)

    # -------------------------------
    # Packet movement logic (separate)
    # -------------------------------
    def move_packet(self, dt):
        direction = self.end_pos - self.pos

        # If already arrived, do nothing
        if direction.length() == 0:
            return

        # Normalize direction safely
        direction = direction.normalize()

        # Move with dt
        self.pos += direction * self.speed * dt

        # Stop at exact end to avoid jump
        if (self.end_pos - self.pos).length() < 1:
            self.pos = Vector2(self.end_pos)

        # Update rect after movement
        self.rect.center = self.pos

    # -------------------------------
    # Called every frame by sprite group
    # -------------------------------
    def update(self, dt):
        self.move_packet(dt)
