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

###################################################################
#FUNKTSIOONID######################################################

#USSI LIIKUMINE
def Ussliigub(ussiklass_Asukoht,suund):
    if suund == 'YLESSE':
        ussiklass_Asukoht[1] -= 10
    if suund == 'ALLA':
        ussiklass_Asukoht[1] += 10
    if suund == 'VASAKULE':
        ussiklass_Asukoht[0] -= 10
    if suund == 'PAREMALE':
        ussiklass_Asukoht[0] += 10

#Joonistab maiustuse
def Maiusjoonista(Maiuseasukoht):
    pygame.draw.rect(Ekraan, pygame.Color(255, 255, 255), pygame.Rect(Maiuseasukoht[0], Maiuseasukoht[1], 10, 10))  

#Joonistab uusi keha
def Ussjoonista(ussiklass_keha):
    for pos in ussiklass_keha:
        pygame.draw.rect(Ekraan, pygame.Color(0, 255, 0),pygame.Rect(pos[0], pos[1], 10, 10))

#Funktsioon millega toimub ussi keha kasvamine, keha järele liikumine ja tagastab true kui sööb maiustuse ära
def Usskasvab(ussiklass_Keha,ussiklass_Asukoht,Randomiga):
    #Lisatakse kehale 1 suurust juurde
    ussiklass_Keha.insert(0,list(ussiklass_Asukoht))
    if ussiklass_Asukoht[0] == Randomiga[0] and ussiklass_Asukoht[1] == Randomiga[1]:
        return True
    else:
    #Et ussi saba tuleks temaga järgi
        ussiklass_Keha.pop()

#Funktsioonmis määrab maiuse random asukoha
def Maiusrandom():
    Randomkoht = [random.randrange(1, (Ekraani_K6rgus//10))* 10,
                    random.randrange(1, (Ekraani_Laius)//10) * 10]
    return Randomkoht
#Funktsioon kui uss läheb vastu seina
def Ussvastuseina(ussiklass_Asukoht,Ekraani_X, Ekraani_Y):
    if ussiklass_Asukoht[0] < 0 or ussiklass_Asukoht[0] > Ekraani_X-10 or ussiklass_Asukoht[1] < 0 or ussiklass_Asukoht[1] > Ekraani_Y-10:
        return True

#Funktsioon kui uss läheb vastu ennast
def Ussvastuennast(ussiklass_Keha,ussiklass_Asukoht):
    for block in ussiklass_Keha[1:]:
        if ussiklass_Asukoht[0] == block[0] and ussiklass_Asukoht[1] == block[1]:
            return True

#Funktsioon mille abil kuvame punkte ekraanil
def Punktiseis():
    pygame.font.init()
    P_font = pygame.font.SysFont('times new roman', 20)
    P_taust = P_font.render(' Punktid : ' + str(Punktid), True, (255, 255, 255))
    P_rect = P_taust.get_rect()
    Ekraan.blit(P_taust, P_rect)

#M2ng l2bi funktsioon
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




##################################################################
###Testid###
#kui uss läheb vastu seina
def Test1():
    TestUss = Ussike(15,[40, 10],[[40, 10],
        [30, 10],
        [20, 10],
        [10, 10]])
    
    Ussliigub(TestUss.Ussi_asukoht, "PAREMALE")
    if Ussvastuseina(TestUss.Ussi_asukoht,50,20)== True:
        return "Test 1 passed"
    else:
        return "Test 1 failed"

#Uss sööb maiuse ära ja sõidab endale sisse
def Test2():
    TestUss= Ussike(15,[100, 50],[[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]])

    Toidu_Asukoht=[110,50]
    Ussliigub(TestUss.Ussi_asukoht, "PAREMALE")
    #uss peab sööma ära maiustuse ja ta keha kasvab
    if Usskasvab(TestUss.Ussi_keha,TestUss.Ussi_asukoht, Toidu_Asukoht)== True:
        #Testib, et keha muutus pikemaks
        if len(TestUss.Ussi_keha)==5:
            #muudab suunda kuniks uss söidab endale sisse
            Ussliigub(TestUss.Ussi_asukoht, "YLESSE")
            TestUss.Ussi_keha.pop()
            Ussliigub(TestUss.Ussi_asukoht, "VASAKULE")
            TestUss.Ussi_keha.pop()
            Ussliigub(TestUss.Ussi_asukoht, "ALLA")
            TestUss.Ussi_keha.pop()
            #Kontrollib kas uss sõitis enda kehale sisse
            if Ussvastuennast(TestUss.Ussi_keha,TestUss.Ussi_asukoht) ==True:
                return "Test 2 passed"
    else:
        return "Test 2 failed"

#Maiuse asukoht oleks erinev eelnevast
def Test3():
    Eelmine=Maiusrandom()
    if not Maiusrandom() == Eelmine:
        return "Test 3 passed"
    else:
        return "Test 3 failed"       
  
print(Test1())
print(Test2())
print(Test3())


#Ussimängu algus####################################################
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
    Rndm=Maiusrandom()
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
        Ussliigub(uss.Ussi_asukoht, suund)

        #Ussi kasvamine kui soob maiuse
        if Usskasvab(uss.Ussi_keha,uss.Ussi_asukoht,Rndm)== True:
            Punktid=Punktid+10
            maiuse_spawn = False

        #Juhul kui maiust ei ole veel
        if not maiuse_spawn:
                Rndm=Maiusrandom()
        
        maiuse_spawn = True

        Ekraan.fill(pygame.Color(0, 0, 0))

        #Ussi joonistamine
        Ussjoonista(uss.Ussi_keha)

        #Maiuse joonistamine
        Maiusjoonista(Rndm)
    
        #Kui uss läheb vastu seina, siis mäng lõppeb -------------------------------------------------
        if Ussvastuseina(uss.Ussi_asukoht,Ekraani_K6rgus,Ekraani_Laius) == True:
            M2ngL2bi()

        #Kui uss läheb iseenda vastu, siis mäng lõppeb -----------------------------------------------
        if Ussvastuennast(uss.Ussi_keha,uss.Ussi_asukoht) == True:
                M2ngL2bi()
        #Punktide kuvamine
        Punktiseis()

        # Refreshimine
        pygame.display.update()
        # Fps
        fps.tick(uss.Ussi_kiirus)


ussim2ng()
     