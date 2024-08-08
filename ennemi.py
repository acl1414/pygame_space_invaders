import pygame as py

from constantes import Constantes
from missile import Missile

 
class Ennemi():

    
    direction_left = False
    direction_down = False

    # INITIALIZATION 
    def __init__(self, x, y, num_ennemi):
        
        self.x = x
        self.y = y

        self.vitesse = 1
      
        self.height=33
        self.width=45

        if (num_ennemi == 1) :
            imageTemp=py.image.load('assets/ennemi1_1.png')
        elif (num_ennemi == 2) :
            imageTemp=py.image.load('assets/ennemi2_1.png')
        else :    
            imageTemp=py.image.load('assets/ennemi3_1.png')

        self.image=py.transform.scale(imageTemp,(self.width*1.5 ,self.height*1.5))
      
        self.CurrentState = 1
        #son
        py.mixer.init()
        py.mixer.music.load("assets/shoot.wav")



    def update(self):

        if (Ennemi.direction_left) :
            self.x = self.x - self.vitesse
        else :    
            self.x = self.x + self.vitesse

        if (self.x < 0 or self.x > (Constantes.width - self.width)) :
            Ennemi.direction_left = not  Ennemi.direction_left
            Ennemi.direction_down = True

    def down(self) :
        self.y = self.y + Constantes.height_line

        



    def display(self, screen):

        screen.blit(self.image , (self.x, self.y))
    
    def move_left(self):

        self.x=self.x - self.vitesse
        if (self.x<0) :
            self.x=0

    
    def move_right(self):

        self.x=self.x + self.vitesse
        if (self.x > Constantes.width - self.wifth) :
            self.x = Constantes.width - self.wifth



    def tir(self, list_missile) :
        if (len(list_missile)==0) :
          list_missile.append(Missile(self.x, self.y, 5))
          #print ("TIR", len(list_missile))    
          py.mixer.music.play()
 




    