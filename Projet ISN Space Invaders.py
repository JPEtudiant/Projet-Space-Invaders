import pygame
import random
pygame.init()

# coding: utf-8
#Creation de la fenetre
win = pygame.display.set_mode((900,600))
pygame.display.set_caption("Stargate")

#importation des images : fond, vaisseau, barre de vie, alien, balle, musique
bg = pygame.image.load('BG.jpg')
char = pygame.image.load('Vaisseau.png')
alien1sprite = pygame.image.load('Alien1.png')
lifebar = pygame.image.load('Barre_de_vie2.png')
spriteballe = pygame.image.load('balle.png')
son = pygame.mixer.Sound("Musique jeu.ogg")
playzone = pygame.Rect(0,0,900,600)

#Definition des caract?ristiques du vaisseau
class Vaisseau(object):
    def __init__(self,x,y,width,height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.hitbox = (self.x, self.y, 64, 64)

    def draw(self,win):
        win.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 15,self.y+15, 70, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 3)


#Definition des caract?ristiques de l'alien
class Alien(object):
    def __init__(self,x,y,width,height,vel,CoinDroite):
        self.x= x
        self.y= y
        self.vel = vel
        self.width = width
        self.height = height
        self.CoinDroite = CoinDroite
        self.hitbox = (self.x, self.y, 64, 64)
        self.touche = pygame.draw.rect(win, (255,0,0), self.hitbox, 3)

    def mouv_alea(self):
        if self.x == -500:
            self.x += 0
        else:
            if self.CoinDroite == True:
                self.x -= self.vel
            else:
                self.x += self.vel

            if self.x <= 30:
                self.CoinDroite = False
                self.y += 40
            if self.x >= 870 - self.width:
                self.CoinDroite = True
                self.y += 40

    def hit(self):
        Rect = self.hitbox
        for bullet in bullets:
            if Rect.colliderect(bullet.hitbox) == True:
                self.x = -500
                self.y = -500

    def draw(self,win):
        self.hit()
        self.mouv_alea()
        win.blit(alien1sprite, (self.x, self.y))
        self.hitbox = pygame.Rect(self.x + 7, self.y +7 , 92, 70)
        self.touche


#Definition des caract?ristiques de la barre de vie
class Lifebar(object):
    def __init__(self,x,y,width,height,vel):
        self.x= x
        self.y= y
        self.width = width
        self.height = height
        self.vel = vel
    def draw(self,win):
        win.blit(lifebar, (self.x, self.y))

#Definition des caract?ristiques du tir
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x, self.y, 64, 64)

    def draw(self,win):
        pygame.draw.rect(win, (255,0,0), self.hitbox, 3)
        win.blit(spriteballe, (self.x, self.y))

#Caract?ristiques de chaque objet affich? dans la page (position x, position y, largeur, longueur, vitesse)
Vaisseau = Vaisseau(50,50,65,60,10)
Alien1 = Alien(400,150,100,80,3,False)
Alien2 = Alien(500,150,100,80,3,False)
Alien3 = Alien(600,150,100,80,3,True)
Alien4 = Alien(300,150,100,80,3,False)
Alien5 = Alien(200,150,100,80,3,False)
Alien6 = Alien(100,150,100,80,3,False)
Alien7 = Alien(700,150,100,80,3,False)
Alien8 = Alien(100,10,100,80,3,True)
Alien9 = Alien(200,10,100,80,3,False)
Alien10 = Alien(300,10,100,80,3,False)
Alien11 = Alien(400,10,100,80,3,False)
Alien12 = Alien(500,10,100,80,3,False)
Alien13 = Alien(600,10,100,80,3,False)
Alien14 = Alien(700,10,100,80,3,False)
Lifebar = Lifebar(20,10,40,60,15)
Projectile1 = projectile(550,30,10,40,2)
bullets = []
son.play()

#Definition de la fenetre de victoire
def WinGame():
    endwin = pygame.display.set_mode((900,600),DisplayMode)
    bgwin = pygame.image.load('bgwin.png')
    clockend = pygame.time.Clock()
    endrun = True

    def redrawEndWindow():
            endwin.blit(bgwin, (0,0))
            pygame.display.update()

    while endrun:
            clockend.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endrun = False
            endkeys = pygame.key.get_pressed()

            if endkeys[pygame.K_ESCAPE]:
                endrun = False

            redrawEndWindow()

    pygame.quit()

#gamewin = 0
#global gamewin

#Definition de l'?cran de jeu
def MainGame():
    def redrawGameWindow () :
        win.blit(bg, (0,0))
        Lifebar.draw(win)
        Projectile1.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        Alien1.draw(win)
        Alien2.draw(win)
        Alien3.draw(win)
        Alien4.draw(win)
        Alien5.draw(win)
        Alien6.draw(win)
        Alien7.draw(win)
        Alien8.draw(win)
        Alien9.draw(win)
        Alien10.draw(win)
        Alien11.draw(win)
        Alien12.draw(win)
        Alien13.draw(win)
        Alien14.draw(win)
        Vaisseau.draw(win)


        pygame.display.update()



    #mainloop (Boucle Principale)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        if playzone.contains(Alien1.hitbox) or playzone.contains(Alien2.hitbox) or playzone.contains(Alien3.hitbox) or playzone.contains(Alien4.hitbox) or playzone.contains(Alien5.hitbox) or playzone.contains(Alien6.hitbox) or playzone.contains(Alien7.hitbox) or playzone.contains(Alien8.hitbox) or playzone.contains(Alien9.hitbox) or playzone.contains(Alien10.hitbox) or playzone.contains(Alien11.hitbox) or playzone.contains(Alien12.hitbox) or playzone.contains(Alien13.hitbox) or playzone.contains(Alien14.hitbox)== 1:
            run = True
            global gamewin
            gamewin = 0

        else:
            gamewin = 1
            run = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and Vaisseau.x > Vaisseau.vel:
            Vaisseau.x -= Vaisseau.vel

        if keys[pygame.K_RIGHT] and Vaisseau.x < 880 - (Vaisseau.width + Vaisseau.vel) :
           Vaisseau.x += Vaisseau.vel

        if keys[pygame.K_UP] and Vaisseau.y > Vaisseau.vel:
           Vaisseau.y -= Vaisseau.vel

        if keys[pygame.K_DOWN] and Vaisseau.y < 585 - (Vaisseau.height - Vaisseau.vel):
           Vaisseau.y += Vaisseau.vel

        for bullet in bullets:
            if bullet.y < 900 and bullet.y > 0:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        facing = 1

        if keys[pygame.K_SPACE]:

            if len(bullets) < 5:
                bullets.append(projectile(round(Vaisseau.x+ 20 ), round(Vaisseau.y +20), 6, (0,0,0), facing))

        if keys[pygame.K_ESCAPE]:
            run = False


#Recollage et rafraichissement


        redrawGameWindow( )

MainGame()

#Condition de victoire et d?faite
#if gamewin == 1:
    #WinGame()
    #pygame.quit()
#else:
    #pygame.quit()