import pygame 
import random

pygame.init

#################################################################
Ussi_kiirus=15

Ekraani_K6rgus= 720
Ekraani_Laius= 480

pygame.display.set_caption("V6imas Ussim2ng!")



fps=pygame.time.Clock()
##################################################################

Ussi_asukoht = [100, 50]

Ussi_keha = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]]
suund = 'PAREMALE'
Viimane_suund = suund




###################################################################
while True:
    Ekraan = pygame.display.set_mode((Ekraani_K6rgus,Ekraani_Laius))

    for event in pygame.event.get():
        #Et saaks ekraani panna "x" kinni
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #Noolte sisendid
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Viimane_suund = 'YLESSE'
            if event.key == pygame.K_DOWN:
                Viimane_suund = 'ALLA'
            if event.key == pygame.K_LEFT:
                Viimane_suund = 'VASAKULE'
            if event.key == pygame.K_RIGHT:
                Viimane_suund = 'PAREMALE'
    
        #Et saaks programmi x kaudu kinni panna


    #Et uss saaks kindlas suunas liikuda ja ei kirjutaks kahte suunda üle
    if Viimane_suund == 'YLESSE' and suund != 'ALLA':
        suund = 'YLESSE'
    if Viimane_suund == 'ALLA' and suund != 'YLESSE':
        suund = 'ALLA'
    if Viimane_suund == 'VASAKULE' and suund != 'PAREMALE':
        suund = 'VASAKULE'
    if Viimane_suund == 'PAREMALE' and suund != 'VASAKULE':
        suund = 'PAREMALE'
    #Ussi suunamine 
    if suund == 'YLESSE':
        Ussi_asukoht[1] -= 10
    if suund == 'ALLA':
        Ussi_asukoht[1] += 10
    if suund == 'VASAKULE':
        Ussi_asukoht[0] -= 10
    if suund == 'PAREMALE':
        Ussi_asukoht[0] += 10
        
    #########################
    Ekraan.fill(pygame.Color(0, 0, 0))

    #Ussi asukoha joonistamine
    Ussi_keha.insert(0, list(Ussi_asukoht))
    for pos in Ussi_keha:
        pygame.draw.rect(Ekraan, pygame.Color(0, 255, 0),pygame.Rect(pos[0], pos[1], 10, 10))

    #Et ussi saba tuleks temaga järgi
    Ussi_keha.pop()













    # Refreshimine
    pygame.display.update()
    # Fps
    fps.tick(Ussi_kiirus)



 
            
            