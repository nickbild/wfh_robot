import pygame
import pygame.camera
import pygame.image


pygame.camera.init()
#camlist = pygame.camera.list_cameras()
cam = pygame.camera.Camera("/dev/video0", (640,480))
cam.start()
# Warm up camera.
img = cam.get_image()

for i in range(10):
    print(i)
    img = cam.get_image()
    pygame.image.save(img, 'abc.bmp')

