import pygame
import random
import math
from pygame import mixer

pygame.init()

ekran=pygame.display.set_mode((800,600))

#arkaplan
arkaplan=pygame.image.load("arkaplan.png")

#arkaplan ses
mixer.music.load("arkaplan.mp3")
mixer.music.play(-1)

#oyun adı ve simge
pygame.display.set_caption("Elegans Virus Oyunu")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#karakter
karakter_resmi=pygame.image.load("karakter.png")

karakterX=370
karakterY=450
karakterX_degistir=0




#virüs
virus_resmi=[]
virusX=[]
virusY=[]
virusX_degistir=[]
virusY_degistir=[]
virus_sayisi=6

for i in range(virus_sayisi):


	virus_resmi.append(pygame.image.load("virus.png"))
	virusX.append(random.randint(0,736))
	virusY.append(random.randint(50,150))
	virusX_degistir.append(3)
	virusY_degistir.append(40)

#mermi
mermi_resmi=pygame.image.load("mermi.png")
mermiX=0
mermiY=480
mermiX_degistir=0
mermiY_degistir=10
mermi_durum="hazır"


#Skor

skor_degeri=0
yazi_tipi=pygame.font.Font("ceerl.ttf",32)

yaziX=10
yaziY=10

def skoru_goster(x,y):
	score=yazi_tipi.render("Skor:"+str(skor_degeri),True,(64,65,104))
	ekran.blit(score,(x,y))

tipi=pygame.font.Font("ceerl.ttf",64)

def oyun_sonu():
	yazi=tipi.render("OYUN SONU",True,(64,65,104))
	ekran.blit(yazi,(200,250))


def virus(x,y,i):
	ekran.blit(virus_resmi[i],(x,y))



def oyuncu(x,y):
	ekran.blit(karakter_resmi,(x,y))

def ates_et(x,y):
	global mermi_durum
	mermi_durum="ates"
	ekran.blit(mermi_resmi,(x+16,y+10))

def mermi_carpmasi(virusX,virusY,mermiX,mermiY):
	mesafe=math.sqrt((math.pow(virusX-mermiX,2))+((math.pow(virusY-mermiY,2))))
	if mesafe < 27:
		return True
	else:
		return False

#oyun döngüsü
running=True
while running:
	ekran.fill((0,0,0))
	#arkaplan
	ekran.blit(arkaplan,(0,0))

	for event in pygame.event.get():
		#tuşlar
		if event.type == pygame.QUIT:
			running=False

		if event.type==pygame.KEYDOWN:
			if event.key ==pygame.K_LEFT:
				karakterX_degistir -= 5

			if event.key==pygame.K_RIGHT:
				karakterX_degistir += 5

			if event.key==pygame.K_SPACE:
				silah_sesi=mixer.Sound("silahsesi.wav")
				silah_sesi.play()
				if mermi_durum is "hazır":
					mermiX=karakterX
					ates_et(mermiX,mermiY)
				

		if event.type==pygame.KEYUP:
			if event.key== pygame.K_LEFT or event.key==pygame.K_RIGHT:
				karakterX_degistir=0
									

	#harita sınırları..

	#karakter hareketi
	karakterX += karakterX_degistir

	if karakterX <=0:
		karakterX=0
	elif karakterX >=736: #karakter boyutu 64*64 oldugundan !
		karakterX=736

	#virus hareketi

	for i in range(virus_sayisi):

		if virusY[i] >400:
			for j in range(virus_sayisi):
				virusY[j]=2000
			oyun_sonu()
			break

		virusX[i]+=virusX_degistir[i]
		if virusX[i] <=0:
			virusX_degistir[i]= 3
			virusY[i]+=virusY_degistir[i]
		elif virusX[i] >=736: #karakter boyutu 64*64 oldugundan !
			virusX_degistir[i]= -3
			virusY[i]+=virusY_degistir[i]

		#carpısma
		carpisma=mermi_carpmasi(virusX[i],virusY[i],mermiX,mermiY)

		if carpisma:
			mermiY=480
			mermi_durum="hazır"
			skor_degeri+=1
			virusX[i]=random.randint(0,736) #spawn oluşturmak için
			virusY[i]=random.randint(50,150)

		virus(virusX[i],virusY[i],i)

	#Mermi hareketi
	if mermiY <=0:
		mermiY=480
		mermi_durum="hazır"


	if mermi_durum is "ates":
		ates_et(mermiX,mermiY)
		mermiY -= mermiY_degistir


	

	oyuncu(karakterX,karakterY)
	skoru_goster(yaziX,yaziY)
	pygame.display.update()
 
