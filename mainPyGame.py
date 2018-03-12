import pygame, sys
from pygame.locals import *
import enigma as en

def main(gear1or, gear2or, gear3or, plugSets):	
	pygame.init()
	pygame.font.init()
	global display
	display = pygame.display.set_mode((1200, 600))
	pygame.display.set_caption("Enigma Machine")
	display.fill((48,48,48))
	display.blit(pygame.image.load("imgs/side.png"), (0,0))
	display.blit(pygame.image.load("imgs/side.png"), (1170,0))
	dict = {}
	for i in range(65,91):
		dict["colour{0}".format(chr(i))] = (255,255,255)
	while 1:
		for event in pygame.event.get():

			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN and event.key < 123 and event.key > 96:
				inputChar = chr(event.key).upper()
				if inputChar in plugSets:
					if plugSets.index(inputChar) % 2 == 0:
						inputChar = plugSets[plugSets.index(inputChar) + 1]
					else:
						inputChar = plugSets[plugSets.index(inputChar) - 1]
				print(inputChar)
				output = en.encrypt(inputChar, gear1or, gear2or, gear3or)
				dict["colour{0}".format(output)] = (255,255,0)
				gear1or = en.incrementGear1(gear1or)
				gear2or = en.incrementGear2(gear1or, gear2or)
				gear3or = en.incrementGear3(gear1or, gear2or, gear3or)
				
			if event.type == pygame.KEYUP:
				for i in range(65,91):
					dict["colour{0}".format(chr(i))] = (255,255,255)

			if gear1or < 9: gear1cord = 277.5
			else: gear1cord = 256
			if gear2or < 9: gear2cord = 400
			else: gear2cord = 380
			if gear3or < 9: gear3cord = 522.5
			else: gear3cord = 475 

			pygame.draw.circle(display, dict["colourQ"], (100, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/Q.png").convert_alpha(), (100,100)), (50,200))
			pygame.draw.circle(display, dict["colourW"], (225, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/W.png").convert_alpha(), (100,100)), (175,200)) #FIX
			pygame.draw.circle(display, dict["colourE"], (350, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/gearChange.png").convert_alpha(), (100,163)), (237.5,20))
			display.blit(pygame.font.SysFont('Arial', 50).render(str(gear1or+1),1,(0,0,0)),(gear1cord,70))
			display.blit(pygame.transform.scale(pygame.image.load("imgs/E.png").convert_alpha(), (100,100)), (300,200))
			pygame.draw.circle(display, dict["colourR"], (475, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/gearChange.png").convert_alpha(), (100,163)), (362.5,20))
			display.blit(pygame.font.SysFont('Arial', 50).render(str(gear2or+1),1,(0,0,0)),(gear2cord,70))
			display.blit(pygame.transform.scale(pygame.image.load("imgs/R.png").convert_alpha(), (100,100)), (425,200)) #FIX
			pygame.draw.circle(display, dict["colourT"], (600, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/gearChange.png").convert_alpha(), (100,163)), (487.5,20))
			display.blit(pygame.font.SysFont('Arial', 50).render(str(gear3or+1),1,(0,0,0)),(gear3cord,70))
			display.blit(pygame.transform.scale(pygame.image.load("imgs/T.png").convert_alpha(), (100,100)), (550,200))
			pygame.draw.circle(display, dict["colourZ"], (725, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/Z.png").convert_alpha(), (100,100)), (675,200))
			pygame.draw.circle(display, dict["colourU"], (850, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/U.png").convert_alpha(), (100,100)), (800,200))
			pygame.draw.circle(display, dict["colourI"], (975, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/I.png").convert_alpha(), (100,100)), (925,200))
			pygame.draw.circle(display, dict["colourO"], (1100, 250), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/O.png").convert_alpha(), (100,100)), (1050,200))
			pygame.draw.circle(display, dict["colourA"], (162, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/A.png").convert_alpha(), (100,100)), (112.5,325))
			pygame.draw.circle(display, dict["colourS"], (287, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/S.png").convert_alpha(), (100,100)), (237.5,325))
			pygame.draw.circle(display, dict["colourD"], (412, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/D.png").convert_alpha(), (100,100)), (362.5,325))
			pygame.draw.circle(display, dict["colourF"], (537, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/F.png").convert_alpha(), (100,100)), (487.5,325))
			pygame.draw.circle(display, dict["colourG"], (662, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/G.png").convert_alpha(), (100,100)), (612.5,325))
			pygame.draw.circle(display, dict["colourH"], (787, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/H.png").convert_alpha(), (100,100)), (737.5,325))
			pygame.draw.circle(display, dict["colourJ"], (912, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/J.png").convert_alpha(), (100,100)), (862.5,325))
			pygame.draw.circle(display, dict["colourK"], (1037, 375), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/K.png").convert_alpha(), (100,100)), (987.5,325))
			pygame.draw.circle(display, dict["colourP"], (100, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/P.png").convert_alpha(), (100,100)), (50,450))
			pygame.draw.circle(display, dict["colourY"], (225, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/Y.png").convert_alpha(), (100,100)), (175,450))
			pygame.draw.circle(display, dict["colourX"], (350, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/X.png").convert_alpha(), (100,100)), (300,450))
			pygame.draw.circle(display, dict["colourC"], (475, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/C.png").convert_alpha(), (100,100)), (425,450))
			pygame.draw.circle(display, dict["colourV"], (600, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/V.png").convert_alpha(), (100,100)), (550,450))
			pygame.draw.circle(display, dict["colourB"], (725, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/B.png").convert_alpha(), (100,100)), (675,450))
			pygame.draw.circle(display, dict["colourN"], (850, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/N.png").convert_alpha(), (100,100)), (800,450))
			pygame.draw.circle(display, dict["colourM"], (975, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/M.png").convert_alpha(), (100,100)), (925,450))
			pygame.draw.circle(display, dict["colourL"], (1100, 500), 49, 0)
			display.blit(pygame.transform.scale(pygame.image.load("imgs/L.png").convert_alpha(), (100,100)), (1050,450))

			pygame.display.update()
			pygame.time.Clock().tick(60)
