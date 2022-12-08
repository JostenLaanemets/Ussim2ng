import pygame 
import random
import time
#######pygame######
pygame.init()
pygame.font.init()
#################################################################
#Ekraani seadistus
Ekraani_K6rgus= 720
Ekraani_Laius= 480
Ekraan = pygame.display.set_mode((Ekraani_K6rgus,Ekraani_Laius))
pygame.display.set_caption("V6imas Ussim2ng!")
fps=pygame.time.Clock()

##################################################################
#ussile klassi loomine
class Ussike:
    def __init__(self,kiirus,asukoht,keha):
        self.Ussi_kiirus=kiirus
        self.Ussi_asukoht = asukoht
        self.Ussi_keha = keha 


#Testib, et mäng lõppeks kui uss läheb vastu seina
def Test2():


    usstest = Ussike(15,[80, 10],[[80, 10],
        [70, 10],
        [60, 10],
        [50, 10]])

    #################################################################
    while True:
            
        usstest.Ussi_asukoht[0] += 10
        usstest.Ussi_keha.insert(0,list(usstest.Ussi_asukoht))

        if usstest.Ussi_asukoht[0] < 0 or usstest.Ussi_asukoht[0] > 30 or usstest.Ussi_asukoht[1] < 0 or usstest.Ussi_asukoht[1] > 80:
            return ("Test 2 passed") 
        else:
            return ("Test 2 failed")           
                 
print(Test2())



##################################################################
#Punktide kuvamine ekraanile
def Punktiseis():
    pygame.font.init()
    P_font = pygame.font.SysFont('times new roman', 20)
    P_taust = P_font.render(' Punktid : ' + str(Punktid), True, (255, 255, 255))
    P_rect = P_taust.get_rect()
    Ekraan.blit(P_taust, P_rect)
    
#Mängu Lõpp
def M2ngL2bi():
    
    Lopu_font = pygame.font.SysFont('times new roman', 50)

    M2ngL2bi_Sonum = Lopu_font.render('Mängus saavutatud punktid : ' +"["+ str(Punktid)+"]", True, (255,0,0))
    Cheeky_Sonum = Lopu_font.render('ggwp, better luck next time!', True, (255,255,255))

    M2ngL2bi_Ruut = M2ngL2bi_Sonum.get_rect()
    Cheeky_Ruut= Cheeky_Sonum.get_rect()

    Cheeky_Ruut.midtop=(360, 200)
    M2ngL2bi_Ruut.midtop = (360, 120)

    Ekraan.blit(M2ngL2bi_Sonum, M2ngL2bi_Ruut)
    Ekraan.blit(Cheeky_Sonum,Cheeky_Ruut)

    pygame.display.flip()

    time.sleep(3)
    pygame.quit()
####################################################################


#Ussimängu algus
def ussim2ng():
    
    global Punktid
    Punktid=0
    #################################################################

    uss = Ussike(15,[100, 50],[[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]])
    #################################################################

    #Ussi algne suund
    suund = 'PAREMALE'
    Viimane_suund = suund
    #################################################################

    #maius
    maiuse_asukoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                    random.randrange(1, (Ekraani_Laius)//10) * 10]
    maiuse_spawn = True
    #################################################################
    while True:
        #Et saaks Mängu ristist kinni panna
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
        #Maiuse joonistamine
        pygame.draw.rect(Ekraan, pygame.Color(255, 255, 255), pygame.Rect(maiuse_asukoht[0], maiuse_asukoht[1], 10, 10))
    

    
        #Kui uss läheb vastu seina, siis mäng lõppeb -------------------------------------------------
        if uss.Ussi_asukoht[0] < 0 or uss.Ussi_asukoht[0] > Ekraani_K6rgus-10 or uss.Ussi_asukoht[1] < 0 or uss.Ussi_asukoht[1] > Ekraani_Laius-10:
            M2ngL2bi()
        #Kui uss läheb iseenda vastu, siis mäng lõppeb -----------------------------------------------
        for block in uss.Ussi_keha[1:]:
            if uss.Ussi_asukoht[0] == block[0] and uss.Ussi_asukoht[1] == block[1]:
                M2ngL2bi()
        #Punktide kuvamine
        Punktiseis()

        # Refreshimine
        pygame.display.update()
        # Fps
        fps.tick(uss.Ussi_kiirus)


ussim2ng()
     