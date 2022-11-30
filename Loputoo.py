import pygame 
import random

Ussi_kiirus=15
Ekraani_K6rgus= 720
Ekraani_Laius= 480

fps=pygame.time.Clock()

pygame.init

pygame.display.set_caption("V6imas Ussim2ng!")
while True:
    Ekraan = pygame.display.set_mode((Ekraani_K6rgus,Ekraani_Laius))
    




    
    for event in pygame.event.get():
        #Et saaks programmi x kaudu kinni panna
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            