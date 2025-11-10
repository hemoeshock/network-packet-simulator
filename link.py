import pygame
import math

class Link:
     def __init__(self, node_a, node_b, color="black", width=3):
        self.node_a = node_a
        self.node_b = node_b
        self.color = color
        self.width = width
        self.start = None
        self.end = None

     def draw(self, display_sur):
        a = self.node_a.rect
        b = self.node_b.rect

        anchors_a = [a.midleft, a.midright, a.midtop, a.midbottom]
        anchors_b = [b.midleft, b.midright, b.midtop, b.midbottom]

        best_pair = (a.center, b.center)
        best_dist = float("inf")

        for pa in anchors_a:
            for pb in anchors_b:
                d = math.dist(pa, pb)
                if d < best_dist:
                    best_dist = d
                    best_pair = (pa, pb)

        self.start, self.end = best_pair
        pygame.draw.line(display_sur, self.color, (int(self.start[0]), int(self.start[1])), (int(self.end[0]), int(self.end[1])), self.width)






'''old code
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
        
        # find x coord max,min for obj a,b
        xa_max = a.right
        xa_min = a.left
        xb_max = b.right
        xb_min = b.left
        # find y coord max,min for obj a,b
        ya_max = a.bottom
        ya_min = a.top
        yb_max = b.bottom
        yb_min = b.top

        # coord ponits for start of short link
        start_x = min(xa_max,max(xa_min,(xb_min+xb_max)/2))
        start_y = min(ya_max,max(ya_min,(yb_min+yb_max)/2))

        # coord ponits for start of short link
        end_x = min(xb_max,max(xb_min,(xa_min+xa_max)/2))
        end_y = min(yb_max,max(yb_min,(ya_min+ya_max)/2))

        start = (int(start_x),int(start_y))
        end = (int(end_x), int(end_y))

        pygame.draw.line(display_sur, self.color, start, end, self.width)'''