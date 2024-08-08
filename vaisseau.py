import pygame as py

from constantes import Constantes
from missile import Missile

 
class Vaisseau():
 
    # INITIALIZATION 
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

        self.vitesse = 5
      
        self.height=50
        self.wifth=50
        imageTemp=py.image.load('assets/vaisseau.png')
        self.image=py.transform.scale(imageTemp,(50,50))
      
        self.CurrentState = 1
        #son
        py.mixer.init()
        py.mixer.music.load("assets/shoot.wav")

      

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
 
    