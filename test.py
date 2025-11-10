import pygame
from pygame.math import Vector2

# Initialize Pygame (required for Vector2 to work correctly in some contexts)
pygame.init()

# Create a Vector2 object
my_vector = Vector2(3, 4)  # This vector has a length of 5 (sqrt(3^2 + 4^2))

print(f"Original vector: {my_vector}, Length: {my_vector.length()}")

# Scale the vector to a new length of 10
my_vector.scale_to_length(10)

print(f"Scaled vector: {my_vector}, Length: {my_vector.length()}")

# Create a zero vector
zero_vector = Vector2(0, 0)

# Attempting to scale a zero vector to a non-zero length will raise a ValueError
try:
    zero_vector.scale_to_length(5)
except ValueError as e:
    print(f"Error scaling zero vector: {e}")

# Scaling a zero vector to length 0 is allowed
zero_vector.scale_to_length(0)
print(f"Zero vector scaled to length 0: {zero_vector}, Length: {zero_vector.length()}")