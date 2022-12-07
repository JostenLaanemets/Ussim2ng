import pygame 
import random

pygame.init()

Ekraani_K6rgus= 720
Ekraani_Laius= 480
Ekraan = pygame.display.set_mode((Ekraani_K6rgus,Ekraani_Laius))

pygame.display.set_caption("V6imas Ussim2ng!")
fps=pygame.time.Clock()

##################################################################
class Ussike:
    def __init__(self,kiirus,asukoht,keha):
        self.Ussi_kiirus=kiirus
        self.Ussi_asukoht = asukoht
        self.Ussi_keha = keha 






 



def Punktiseis():

    P_font = pygame.font.SysFont('Times New Roman', 30)
    p_taust = P_font.render('--------------------------|  Punktid : ' + str(Punktid)+'  |----------------------------', True, (255, 255, 255))
    p_rect = p_taust.get_rect()
    Ekraan.blit(p_taust, p_rect)   

def ussim2ng():
    global Punktid
    Punktid=0
    
    uss = Ussike(15,[100, 50],[[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]])
    ###################################################################

    #Ussi algne suund
    suund = 'PAREMALE'
    Viimane_suund = suund
    ###################################################################
    #maius

    maiuse_asukoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                    random.randrange(1, (Ekraani_Laius)//10) * 10]
    maiuse_spawn = True
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
            uss.Ussi_asukoht[1] -= 10
        if suund == 'ALLA':
            uss.Ussi_asukoht[1] += 10
        if suund == 'VASAKULE':
            uss.Ussi_asukoht[0] -= 10
        if suund == 'PAREMALE':
            uss.Ussi_asukoht[0] += 10

        #Ussi kasvamine kui soob maiuse
        uss.Ussi_keha.insert(0,list(uss.Ussi_asukoht))
        if uss.Ussi_asukoht[0] == maiuse_asukoht[0] and uss.Ussi_asukoht[1] == maiuse_asukoht[1]:
            Punktid=Punktid+10
            maiuse_spawn = False
        else:
            #Et ussi saba tuleks temaga järgi
            uss.Ussi_keha.pop()
        #Juhul kui maiust ei ole veel
        if not maiuse_spawn:
            maiuse_asukoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                        random.randrange(1, (Ekraani_Laius)//10) * 10]
        maiuse_spawn = True

        Ekraan.fill(pygame.Color(0, 0, 0))
        #Ussi joonistamine
        for pos in uss.Ussi_keha:
            pygame.draw.rect(Ekraan, pygame.Color(0, 255, 0),pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(Ekraan, pygame.Color(255, 255, 255), pygame.Rect(maiuse_asukoht[0], maiuse_asukoht[1], 10, 10))
    

    
        #Kui uss läheb vastu seina, siis mäng lõppeb -------------------------------------------------
        if uss.Ussi_asukoht[0] < 0 or uss.Ussi_asukoht[0] > Ekraani_K6rgus-10 or uss.Ussi_asukoht[1] < 0 or uss.Ussi_asukoht[1] > Ekraani_Laius-10:
            pygame.quit()
        #Kui uss läheb iseenda vastu, siis mäng lõppeb -----------------------------------------------
        for block in uss.Ussi_keha[1:]:
            if uss.Ussi_asukoht[0] == block[0] and uss.Ussi_asukoht[1] == block[1]:
                pygame.quit()

        Punktiseis()

        # Refreshimine
        pygame.display.update()
        # Fps
        fps.tick(uss.Ussi_kiirus)
ussim2ng()

     