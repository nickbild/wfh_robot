import os
import pygame
import pygame.camera
import pygame.image


# Initialize the camera.
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640,480))
cam.start()

# Warm up camera.
img = cam.get_image()

# Continually refresh image.
while(True):
    img = cam.get_image()
    pygame.image.save(img, 'temp.bmp')
    os.rename('temp.bmp', 'current_view.bmp')
