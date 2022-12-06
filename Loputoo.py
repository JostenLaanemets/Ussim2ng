import pygame 
import random

pygame.init()

#################################################################

Punktid=0

Ekraani_K6rgus= 720
Ekraani_Laius= 480
Ekraan = pygame.display.set_mode((Ekraani_K6rgus,Ekraani_Laius))
pygame.display.set_caption("V6imas Ussim2ng!")


fps=pygame.time.Clock()
##################################################################
Ussi_kiirus=15
Ussi_asukoht = [100, 50]

Ussi_keha = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]]
###################################################################
suund = 'PAREMALE'
Viimane_suund = suund

###################################################################
#maius

maiuse_asukoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                random.randrange(1, (Ekraani_Laius)//10) * 10]
maiuse_spawn = True


def Test1():
    Testing=True
    while Testing:
        pass



def PunktidOn():

    P_font = pygame.font.SysFont('times new roman', 30)
    p_taust = P_font.render('--------------------------|  Punktid : ' + str(Punktid)+'  |----------------------------', True, (255, 255, 255))
    p_rect = p_taust.get_rect()
    Ekraan.blit(p_taust, p_rect)   


###################################################################
while True:
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

    #Ussi kasvamine kui soob maiuse
    Ussi_keha.insert(0,list(Ussi_asukoht))
    if Ussi_asukoht[0] == maiuse_asukoht[0] and Ussi_asukoht[1] == maiuse_asukoht[1]:
        Punktid=Punktid+10
        maiuse_spawn = False
    else:
        #Et ussi saba tuleks temaga järgi
        Ussi_keha.pop()
    #Juhul kui maiust ei ole veel
    if not maiuse_spawn:
        maiuse_asukoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                    random.randrange(1, (Ekraani_Laius)//10) * 10]
    maiuse_spawn = True

    Ekraan.fill(pygame.Color(0, 0, 0))
    #Ussi joonistamine
    for pos in Ussi_keha:
        pygame.draw.rect(Ekraan, pygame.Color(0, 255, 0),pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(Ekraan, pygame.Color(255, 255, 255), pygame.Rect(maiuse_asukoht[0], maiuse_asukoht[1], 10, 10))
  

   
    #Kui uss läheb vastu seina, siis mäng lõppeb -------------------------------------------------
    if Ussi_asukoht[0] < 0 or Ussi_asukoht[0] > Ekraani_K6rgus or Ussi_asukoht[1] < 0 or Ussi_asukoht[1] > Ekraani_Laius:
        pygame.quit()
    #Kui uss läheb iseenda vastu, siis mäng lõppeb -----------------------------------------------
    for block in Ussi_keha[1:]:
        if Ussi_asukoht[0] == block[0] and Ussi_asukoht[1] == block[1]:
            pygame.quit()

    PunktidOn()

    # Refreshimine
    pygame.display.update()
    # Fps
    fps.tick(Ussi_kiirus)

     